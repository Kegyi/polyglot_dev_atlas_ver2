import asyncio

async def fetch(endpoint: str) -> tuple[str, bool, str]:
    await asyncio.sleep(0.05)
    if "fail" in endpoint:
        return endpoint, False, "timeout"
    return endpoint, True, f"{{\"endpoint\": \"{endpoint}\"}}"

async def main() -> None:
    endpoints = ["users", "orders", "fail-metrics"]
    results = await asyncio.gather(*(fetch(ep) for ep in endpoints), return_exceptions=False)

    data = [payload for _, ok, payload in results if ok]
    errors = [f"{ep}: {payload}" for ep, ok, payload in results if not ok]

    print({"data": data, "errors": errors})

asyncio.run(main())
