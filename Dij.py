import sys
import heapq

class vrtx:
    def __init__(self, node):

        self.identity = node

        self.adjacent = {}

        self.dist = sys.maxint
        
	self.vis = False  
        
        self.p = None

    def add_n(self, n, w=0):
        self.adjacent[n] = w

    def get_c(self):
        return self.adjacent.keys()  

    def get_identity(self):
        return self.identity

    def get_w(self, n):
        return self.adjacent[n]

    def set_dist(self, dist):
        self.dist = dist

    def get_dist(self):
        return self.dist

    def set_p(self, prev):
        self.p = prev

    def set_vis(self):
        self.vis = True

    def __str__(self):
        return str(self.identity) + ' adjacent: ' + str([x.identity for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vrtx(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vrtx = vrtx(node)
        self.vert_dict[node] = new_vrtx
        return new_vrtx

    def get_vrtx(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_e(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vrtx(frm)
        if to not in self.vert_dict:
            self.add_vrtx(to)

        self.vert_dict[frm].add_n(self.vert_dict[to], cost)
        self.vert_dict[to].add_n(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_p(self, current):
        self.p = current

    def get_p(self, current):
        return self.p

def shortest(v, path):
    ''' make shortest path from v.p'''
    if v.p:
        path.append(v.p.get_identity())
        shortest(v.p, path)
    return



def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    
    start.set_dist(0)

 
    u_q = [(v.get_dist(),v) for v in aGraph]
    heapq.heapify(u_q)

    while len(u_q):
       
        uv = heapq.heappop(u_q)
        current = uv[1]
        current.set_vis()

        for next in current.adjacent:
            
            if next.vis:
                continue
            new_dist = current.get_dist() + current.get_w(next)
            
            if new_dist < next.get_dist():
                next.set_dist(new_dist)
                next.set_p(current)
                print 'the updated cost : current = %s next = %s new_cost = %s' \
                        %(current.get_identity(), next.get_identity(), next.get_dist())
            else:
                print 'did not update cost : current = %s next = %s new_cost = %s' \
                        %(current.get_identity(), next.get_identity(), next.get_dist())

      
        while len(u_q):
            heapq.heappop(u_q)
        u_q = [(v.get_dist(),v) for v in aGraph if not v.vis]
        heapq.heapify(u_q)
    
if __name__ == '__main__':

    g = Graph()

    g.add_vrtx('S')
    g.add_vrtx('T')
    g.add_vrtx('U')
    g.add_vrtx('V')
    g.add_vrtx('W')
    g.add_vrtx('X')
    g.add_vrtx('Y')
    g.add_vrtx('Z')

    g.add_e('Z', 'T', 2)  
    g.add_e('Z', 'Y', 5)
    g.add_e('T', 'S', 1)
    g.add_e('T', 'Z', 2)
    g.add_e('T', 'W', 9)
    g.add_e('T', 'U', 2)
    g.add_e('T', 'Y', 4)
    g.add_e('Y', 'T', 4)
    g.add_e('Y', 'X', 6)
    g.add_e('Y', 'W', 1)
    g.add_e('Y', 'Z', 5)
    g.add_e('S', 'T', 1)
    g.add_e('S', 'U', 4)
    g.add_e('X', 'Y', 6)
    g.add_e('X', 'W', 3)
    g.add_e('X', 'V', 1)
    g.add_e('V', 'X', 1)
    g.add_e('V', 'W', 1)
    g.add_e('V', 'U', 1)
    g.add_e('U', 'V', 1)
    g.add_e('U', 'W', 1)
    g.add_e('U', 'T', 2)
    g.add_e('U', 'S', 4)
    g.add_e('W', 'U', 1)
    g.add_e('W', 'V', 1)
    g.add_e('W', 'X', 3)
    g.add_e('W', 'T', 9)
    g.add_e('W', 'Y', 1)
	 

    print 'Graph data:'
    for v in g:
        for w in v.get_c():
            videntity = v.get_identity()
            widentity = w.get_identity()
            print '( %s , %s, %3d)'  % ( videntity, widentity, v.get_w(w))

    dijkstra(g, g.get_vrtx('S'), g.get_vrtx('Z')) 

    target = g.get_vrtx('Z')
    path = [target.get_identity()]
    shortest(target, path)
    print 'The shortest path : %s' %(path[::-1])
