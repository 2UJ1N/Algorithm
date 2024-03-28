#include <string>
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <stack>

using namespace std;
#define unMap unordered_map

unMap<int, set<int>> createGraph(const vector<vector<int>>& edges) {
    unMap<int, set<int>> graph;
    for (const auto& edge : edges) {
        int from = edge[0];
        int to = edge[1];
        graph[from].insert(to);
    }
    return graph;
}

vector<int> findUnrelatedVertex(const unMap<int, set<int>>& graph) {
    int maxEdges = 0;
    int unrelatedVertex = -1;
    for (const auto& node : graph) {
        int vertex = node.first;
        int edgeCount = node.second.size();
        if (edgeCount > maxEdges) {
        maxEdges = edgeCount;
        unrelatedVertex = vertex;
        }
    }
    vector<int> returnVector(1, 0);
    returnVector[0] = unrelatedVertex;
    return returnVector;
}

vector<int> findGraphType(const unMap<int, set<int>>& graph, int unrelatedVertex) {
    vector<int> returnVector(3, 0);

    for (int neighbor : graph.at(unrelatedVertex)) {
        int vertexCount = 0;
        int edgeCount = 0;

        set<int> visited;
        stack<int> stack;
        stack.push(neighbor);

        while (!stack.empty()) {
            int current = stack.top();
            stack.pop();

            if (visited.find(current) == visited.end()) {
                visited.insert(current);
                vertexCount++;

                if (graph.find(current) != graph.end()) {
                    edgeCount += graph.at(current).size();
                    for (int adjacent : graph.at(current)) {
                        if (visited.find(adjacent) == visited.end()) {
                            stack.push(adjacent);
                        }
                    }
                }
            }
        }

        if (vertexCount == edgeCount) returnVector[0]++;
        else if (edgeCount == vertexCount - 1) returnVector[1]++;
        else returnVector[2]++;
    }
    return returnVector;
}

vector<int> solution(vector<vector<int>> edges) {
    auto graph = createGraph(edges);
    vector<int> answer = findUnrelatedVertex(graph);
    vector<int> graphTypeCounts = findGraphType(graph, answer[0]);

    // graphTypeCounts의 모든 요소를 answer 벡터에 추가
    answer.insert(answer.end(), graphTypeCounts.begin(), graphTypeCounts.end());

    return answer;
}