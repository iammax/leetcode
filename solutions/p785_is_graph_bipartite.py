class Solution(object):
    def isBipartite(self, graph):
        colordict = {0: 1}
        dim = len(graph)
        unused_nodes = range(0, dim)
        any_last_time = 1
        while len(unused_nodes) > 0:
            if any_last_time == 0:
                colordict[unused_nodes[0]] = 1
            any_last_time = 0
            to_remove = []
            for node in unused_nodes:
                if node in colordict.keys():
                    any_last_time = 1
                    to_remove.append(node)
                    this_color = colordict[node]
                    connections = graph[node]
                    for connection in connections:
                        if connection in colordict.keys():
                            if colordict[connection] == this_color:
                                print 'false, ', connection, node
                                return False		
                        else:
                            colordict[connection] = -1*this_color
                else:
                    connected_colors = []
                    connections = graph[node]
                    for connection in connections:
                        if connection in colordict.keys():
                            connected_color = colordict[connection]
                            if connected_color not in connected_colors:
                                connected_colors.append(connected_color)
                        if len(connected_colors) > 1:
                            return False
                    if len(connected_colors) == 1:
                        to_remove.append(node)
                        colordict[node] = -1*connected_colors[0]
                        any_last_time = 1
                    else:
                        pass
            for node in to_remove:
                unused_nodes.remove(node)
        return True
