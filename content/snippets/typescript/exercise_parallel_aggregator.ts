type Result = { endpoint: string; ok: boolean; payload: string };

async function fetchEndpoint(endpoint: string): Promise<Result> {
  await new Promise((r) => setTimeout(r, 50));
  if (endpoint.includes("fail")) return { endpoint, ok: false, payload: "timeout" };
  return { endpoint, ok: true, payload: JSON.stringify({ endpoint }) };
}

async function main() {
  const endpoints = ["users", "orders", "fail-metrics"];
  const results = await Promise.all(endpoints.map(fetchEndpoint));

  const data = results.filter(r => r.ok).map(r => r.payload);
  const errors = results.filter(r => !r.ok).map(r => `${r.endpoint}: ${r.payload}`);

  console.log({ data, errors });
}

void main();
type Result = { id: number; value: number };

async function fetchResult(id: number): Promise<Result> {
  return new Promise((res) => setTimeout(() => res({ id, value: Math.random() * 100 }), 50));
}

async function parallelAggregate(ids: number[]): Promise<number> {
  const results = await Promise.all(ids.map(fetchResult));
  return results.reduce((sum, r) => sum + r.value, 0);
}

(async () => {
  const total = await parallelAggregate([1, 2, 3, 4, 5]);
  console.log("Total:", total);
})();
