class Solution(object):
    def isBipartite(self, graph):
        colordict = {0: 1}
        dim = len(graph)
        unused_nodes = range(0, dim)
        any_last_time = 1
        while len(unused_nodes) > 0:
       #     print unused_nodes
        #    print colordict	
            if any_last_time == 0:
         #       print 'nothing happened last time, coloring the first'
                colordict[unused_nodes[0]] = 1
            any_last_time = 0
            to_remove = []
            for node in unused_nodes:
          #      print 'trying: ', node
                if node in colordict.keys():
           #         print '{0} is colored'.format(node)
                    any_last_time = 1
                    to_remove.append(node)
                    this_color = colordict[node]
                    connections = graph[node]
            #        print 'connection: ', connections
                    for connection in connections:
                        if connection in colordict.keys():
                            if colordict[connection] == this_color:
                                print 'false, ', connection, node
                                return False		
                        else:
                       #     print "its neighbor {0} is uncolored".format(connection)
                            colordict[connection] = -1*this_color
                else:
               #     print '{0} is uncolored'.format(node)
                    connected_colors = []
                    connections = graph[node]
                    for connection in connections:
                        if connection in colordict.keys():
                            connected_color = colordict[connection]
                            if connected_color not in connected_colors:
                                connected_colors.append(connected_color)
                        if len(connected_colors) > 1:
                         #   return "{0} connected to both".format(node)
                            return False
                    if len(connected_colors) == 1:
                        #print 'but its neighbors all have the same color'
                        to_remove.append(node)
                        colordict[node] = -1*connected_colors[0]
                        any_last_time = 1
                    else:
                        pass
            for node in to_remove:
                unused_nodes.remove(node)
        return True
