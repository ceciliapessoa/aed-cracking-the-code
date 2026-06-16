def has_cycle(graph: dict[str, list[str]]) -> bool:
    visitados = set()
    caminho = set()

    def dfs(no):
        if no in caminho:
            return True

        if no in visitados:
            return False

        visitados.add(no)
        caminho.add(no)

        for vizinho in graph.get(no, []):
            if dfs(vizinho):
                return True

        caminho.remove(no)

        return False

    for no in graph:
        if dfs(no):
            return True

    return False