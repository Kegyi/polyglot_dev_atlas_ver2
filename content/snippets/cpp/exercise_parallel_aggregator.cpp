#include <future>
#include <iostream>
#include <string>
#include <vector>

struct Result {
    std::string endpoint;
    bool ok;
    std::string payloadOrError;
};

Result fetch(const std::string& endpoint) {
    if (endpoint.find("fail") != std::string::npos) {
        return {endpoint, false, "timeout"};
    }
    return {endpoint, true, "{\"endpoint\":\"" + endpoint + "\"}"};
}

int main() {
    std::vector<std::string> endpoints{ "users", "orders", "fail-metrics" };
    std::vector<std::future<Result>> jobs;

    for (const auto& ep : endpoints) {
        jobs.push_back(std::async(std::launch::async, fetch, ep));
    }

    std::vector<std::string> data;
    std::vector<std::string> errors;

    for (auto& j : jobs) {
        Result r = j.get();
        if (r.ok) data.push_back(r.payloadOrError);
        else errors.push_back(r.endpoint + ": " + r.payloadOrError);
    }

    std::cout << "data=" << data.size() << ", errors=" << errors.size() << "\n";
}
