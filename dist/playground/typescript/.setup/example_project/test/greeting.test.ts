import { describe, expect, it } from "vitest";
import { greet } from "../src/greeting.js";

describe("greet", () => {
  it("returns greeting with name", () => {
    expect(greet("Alice")).toBe("Hello, Alice");
  });

  it("returns plain hello for empty string", () => {
    expect(greet("")).toBe("Hello");
  });

  it("returns greeting with world", () => {
    expect(greet("world")).toBe("Hello, world");
  });
});
