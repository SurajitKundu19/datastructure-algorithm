class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_paths(self, start: str, end: str, path: list) -> list:
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                # print(new_paths)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_paths(self, start: str, end: str, path: list) -> list:
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        sp = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_shortest_paths(node, end, path)
                if new_path:
                    if not len(sp) or len(new_path) < len(sp):
                        sp = new_path

        return sp


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "NewYork"),
        ("Paris", "Dubai"),
        ("Dubai", "NewYork"),
    ]
    routes = Graph(routes)
    print(routes.graph_dict)
    print(routes.get_paths("Mumbai", "NewYork", []))
    print(routes.get_shortest_paths("Mumbai", "NewYork", []))
