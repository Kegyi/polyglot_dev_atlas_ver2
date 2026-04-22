import { describe, it, expect } from "vitest";
import { sum, average, max } from "./stats";

describe("sum", () => {
  it("adds values", () => {
    expect(sum([1, 2, 3])).toBe(6);
  });
  it("returns 0 for empty", () => {
    expect(sum([])).toBe(0);
  });
});

describe("average", () => {
  it("computes mean", () => {
    expect(average([1, 2, 3])).toBe(2);
  });
  it("returns 0 for empty", () => {
    expect(average([])).toBe(0);
  });
});

describe("max", () => {
  it("finds largest", () => {
    expect(max([1, 5, 3, 2])).toBe(5);
  });
  it("returns 0 for empty", () => {
    expect(max([])).toBe(0);
  });
});
