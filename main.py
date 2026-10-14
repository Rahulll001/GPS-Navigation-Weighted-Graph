
import heapq

city = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
    "D": [("B", 5), ("C", 8), ("E", 2)],
    "E": [("C", 10), ("D", 2)]
}

def shortest_path(graph, start, end):
    distances = {node: float("inf") for node in graph}
    previous = {}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        distance, node = heapq.heappop(queue)

        if distance > distances[node]:
            continue

        if node == end:
            break

        for neighbor, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                heapq.heappush(queue, (new_distance, neighbor))

    if distances[end] == float("inf"):
        return [], float("inf")

    path = []
    current = end

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return path, distances[end]


start = "A"
end = "E"

path, distance = shortest_path(city, start, end)

print("GPS Navigation System")
print("Starting Point:", start)
print("Destination:", end)
print("Shortest Path:", " -> ".join(path))
print("Total Distance:", distance, "km")
