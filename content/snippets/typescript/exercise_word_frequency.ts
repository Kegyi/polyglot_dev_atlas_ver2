const text = "This is a test. This test is simple.";
const words = (text.toLowerCase().match(/[a-z]+/g) ?? []);

const freq = new Map<string, number>();
for (const w of words) {
  freq.set(w, (freq.get(w) ?? 0) + 1);
}

const items = [...freq.entries()]
  .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));

for (const [word, count] of items) {
  console.log(`${word}: ${count}`);
}
function wordFrequency(text: string) {
  const freq: Record<string, number> = {};
  text.toLowerCase()
    .replace(/[^a-z\s]/g, "")
    .split(/\s+/)
    .filter(Boolean)
    .forEach((w) => (freq[w] = (freq[w] || 0) + 1));
  return freq;
}

console.log(wordFrequency("Hello world hello"));
