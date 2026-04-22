export function sum(values: number[]): number {
  return values.reduce((acc, v) => acc + v, 0);
}

export function average(values: number[]): number {
  if (values.length === 0) return 0;
  return sum(values) / values.length;
}

export function max(values: number[]): number {
  if (values.length === 0) return 0;
  return Math.max(...values);
}
