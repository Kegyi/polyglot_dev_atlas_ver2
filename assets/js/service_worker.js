/**
 * Polyglot Atlas Service Worker
 * Enables offline mode by caching essential resources
 * Cache-first strategy for static assets, network-first for content
 */

const CACHE_VERSION = 'atlas-v1';
const RUNTIME_CACHE = 'atlas-runtime-v1';

// Critical assets to cache on install
const CRITICAL_ASSETS = [
  './',
  './assets/css/main.css',
  './assets/css/ui_states.css',
  './assets/js/app.js',
  './assets/js/selection_engine.js',
  './assets/js/content_renderers.js',
  './assets/js/search_ui.js',
  './assets/js/polyglot_filter.js',
  './assets/js/permalinks.js',
  './assets/hljs/atom-one-dark.min.css',
  './assets/hljs/github.min.css'
];

// Install event: cache critical assets
self.addEventListener('install', event => {
  console.log('[Service Worker] Installing...');
  
  event.waitUntil(
    caches.open(CACHE_VERSION)
      .then(cache => {
        console.log('[Service Worker] Caching critical assets');
        return cache.addAll(CRITICAL_ASSETS);
      })
      .then(() => self.skipWaiting())
      .catch(error => console.error('[Service Worker] Install failed:', error))
  );
});

// Activate event: clean up old caches
self.addEventListener('activate', event => {
  console.log('[Service Worker] Activating...');
  
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames
            .filter(name => name !== CACHE_VERSION && name !== RUNTIME_CACHE)
            .map(name => {
              console.log('[Service Worker] Deleting old cache:', name);
              return caches.delete(name);
            })
        );
      })
      .then(() => self.clients.claim())
      .catch(error => console.error('[Service Worker] Activation failed:', error))
  );
});

// Fetch event: cache-first for assets, network-first for HTML/JSON
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }
  
  // Skip external URLs (cross-origin)
  if (url.origin !== location.origin) {
    return;
  }
  
  // Cache-first strategy for static assets
  if (
    request.url.includes('/assets/') ||
    request.url.includes('/content/locales/') ||
    request.url.endsWith('.css') ||
    request.url.endsWith('.js') ||
    request.url.endsWith('.woff2') ||
    request.url.endsWith('.png') ||
    request.url.endsWith('.svg')
  ) {
    event.respondWith(
      caches.match(request)
        .then(response => {
          if (response) {
            return response;
          }
          return fetch(request)
            .then(response => {
              // Cache successful responses
              if (response && response.status === 200) {
                const cacheName = request.url.includes('/assets/') 
                  ? CACHE_VERSION 
                  : RUNTIME_CACHE;
                const responseClone = response.clone();
                caches.open(cacheName)
                  .then(cache => cache.put(request, responseClone))
                  .catch(error => console.error('[Service Worker] Cache write failed:', error));
              }
              return response;
            })
            .catch(error => {
              console.error('[Service Worker] Fetch failed:', error);
              // Return offline fallback if available
              return caches.match(request)
                .then(cachedResponse => cachedResponse || createOfflinePage());
            });
        })
    );
  }
  // Network-first strategy for HTML and JSON pages
  else if (
    request.url.endsWith('.html') ||
    request.url.endsWith('.json') ||
    request.url.endsWith('/')
  ) {
    event.respondWith(
      fetch(request)
        .then(response => {
          // Cache successful HTML/JSON responses
          if (response && response.status === 200) {
            const responseClone = response.clone();
            caches.open(RUNTIME_CACHE)
              .then(cache => cache.put(request, responseClone))
              .catch(error => console.error('[Service Worker] Cache write failed:', error));
          }
          return response;
        })
        .catch(error => {
          console.error('[Service Worker] Network request failed:', error);
          // Try to return cached version
          return caches.match(request)
            .then(cachedResponse => {
              if (cachedResponse) {
                console.log('[Service Worker] Serving from cache:', request.url);
                return cachedResponse;
              }
              // Return offline fallback
              return createOfflinePage();
            });
        })
    );
  }
});

/**
 * Create a simple offline fallback page
 */
function createOfflinePage() {
  return new Response(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Offline - Polyglot Atlas</title>
      <style>
        body {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
          background: linear-gradient(135deg, #09090b, #18181b);
          color: #fafafa;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
          margin: 0;
          padding: 20px;
        }
        .container {
          text-align: center;
          max-width: 500px;
        }
        h1 {
          font-size: 2.5rem;
          margin: 0 0 10px 0;
          color: #38bdf8;
        }
        p {
          font-size: 1.1rem;
          line-height: 1.6;
          color: #a1a1aa;
          margin: 10px 0;
        }
        .icon {
          font-size: 4rem;
          margin: 20px 0;
        }
        .info {
          background: rgba(255, 255, 255, 0.05);
          border: 1px solid rgba(255, 255, 255, 0.1);
          border-radius: 8px;
          padding: 20px;
          margin: 20px 0;
          font-size: 0.95rem;
          color: #a1a1aa;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="icon">📡</div>
        <h1>You're Offline</h1>
        <p>The Polyglot Atlas Service Worker is active, but this page hasn't been cached yet.</p>
        <p>Try visiting cached pages or reconnect to the internet.</p>
        <div class="info">
          <strong>Service Worker Status:</strong> ✓ Active<br>
          <strong>Cached Pages:</strong> Available offline<br>
          <strong>New Content:</strong> Requires connection
        </div>
        <p style="margin-top: 30px; font-size: 0.9rem; color: #71717a;">
          Go back or try accessing a previously visited page.
        </p>
      </div>
    </body>
    </html>
  `, {
    status: 503,
    statusText: 'Service Unavailable',
    headers: { 'Content-Type': 'text/html; charset=utf-8' }
  });
}

// Message event: handle messages from clients
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
