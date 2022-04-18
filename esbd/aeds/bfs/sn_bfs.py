from math import sqrt
import random
from typing import Dict, List
import uuid
from tqdm import tqdm
import sys
import getopt
from enum import Enum

class Types(str, Enum):
    MALE = "male"
    FEMALE = "female"

class Person(object):

    def __init__(self, uid, s_type):
        self._uid = uid
        self._s_type = s_type

    def get_uid(self):
        return self._uid
    
    def get_s_type(self):
        return self._s_type


class FriendNetwork(object):

    def __init__(self, people_num, connections_num):
        self._people_num = people_num
        self._connections_num = connections_num
        self._graph = self._generate_graph()

    def _generate_graph(self):

        people = []
        for person_index in range(self._people_num):
            uid = str(uuid.uuid4())
            s_type = 'female' if person_index < (self._people_num // 2)  else 'male'
            people.append(Person(uid, s_type))

        conn_num = 0
        graph = {}
        graph_aux = {} # criando um grafo auxiliar para agilizar algumas buscas
        while conn_num < self._connections_num:
            person, friend = random.sample(people, 2)
            person_uid = person.get_uid()
            friend_uid = friend.get_uid()

            if person_uid not in graph:
                graph[person_uid] = {
                    'this': person,
                    'friends': []
                }
                # criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo
                graph_aux[person_uid] = {}

            if friend_uid not in graph:
                graph[friend_uid] = {
                    'this': friend,
                    'friends': []
                }
                # criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo
                graph_aux[friend_uid] = {} 

            # if person_uid == friend_uid or \
            #     friend in graph[person_uid]['friends']: # fazer essa verificação em um índice auxiliar
            #     continue
            if person_uid == friend_uid or \
                friend_uid in graph_aux[person_uid]: # fazer essa verificação em um índice auxiliar
                continue

            graph[person_uid]['friends'].append(friend)
            graph[friend_uid]['friends'].append(person)
            # adicionar vizinho também nos índices do grafo auxiliar
            graph_aux[person_uid][friend_uid] = True
            graph_aux[friend_uid][person_uid] = True
            conn_num += 1

        people_to_remove = []
        for person_uid in graph:
            friends_types = [*map(lambda p: p.get_s_type(), graph[person_uid]['friends'])]
            person_type = graph[person_uid]['this'].get_s_type()
            if ('male' not in friends_types or 'female' not in friends_types) and person_type in friends_types:
                people_to_remove.append({'person_uid': person_uid, 'remove_from': graph[person_uid]['friends']})

        for person_props in people_to_remove:
            for friend in person_props['remove_from']:
                person_index = [*map(lambda friend: friend.get_uid(),
                    graph[friend.get_uid()]['friends'])].index(person_props['person_uid'])
                del graph[friend.get_uid()]['friends'][person_index]
            del graph[person_props['person_uid']]

        return graph
    
    def get_person_by_uid(self, uid):
        return self._graph[uid]['this']
    
    def _search_wtype(self, person_uid, friend_uid):
        '''
        person_uid: start node
        friend_uid: target node
        '''
        path = [person_uid]
        
        visited = {person_uid}
        queue = [person_uid]
        found = False
        
        while queue:
            
            current = queue.pop(0)
            current_type = self._graph[current]["this"]._s_type
            
            if current == friend_uid:
                found = True
                break
            
            for friend in self._graph[person_uid]["friends"]:
                next_node = friend._uid
                next_type = friend._s_type
                if (
                    next_node not in visited and
                    current_type != next_type 
                ):
                    visited.add(next_node)
                    queue.append(next_node)
                    path.append(next_node)
        
        return path         
    
    def _search(self, person_uid, friend_uid):
        '''
        person_uid: start node
        friend_uid: target node
        '''
        
        visited = {person_uid}
        queue = [person_uid]
        parent = {
            person_uid: None
        }
        found = False
        
        while queue:
            
            current = queue.pop(0)
            
            if current == friend_uid:
                found = True
                break
            
            for friend in self._graph[person_uid]["friends"]:
                next_node = friend._uid
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
                    parent[next_node] = current
        
        return visited 
    
    def get_separation_degree(self, search_type: str):
        
        search = {
           "type_1": self._search,
           "type_2": self._search_wtype
        }
    
        total_paths_len = 0

        for _ in range(100):
            person_uid, friend_uid = random.sample([*self._graph.keys()], 2)
            path = search[search_type](person_uid, friend_uid)
            total_paths_len += len(path) - 1

        return total_paths_len / 100


if __name__ == '__main__':

    def get_networks(n: int) -> FriendNetwork:
        ns = {
            "n0": 5*n,
            "n1": int(n*sqrt(n)),
            "n2": int(n*n/5)
        }

        nets = []

        for idx, e in tqdm(ns.items()):
          nets.append(FriendNetwork(int(n),int(e)))
        return nets
        
    def networks(n) -> Dict[int, List[FriendNetwork]]:
        vertexes = [n]  # [100, 1000, 100000, 100000]
        nets = {v: get_networks(v) for v in tqdm(vertexes, "Creating networks")}
        return nets
        
    n = int(sys.argv[1])
    search_type = (sys.argv[2])
    print(f" Starting Separation Degree calculation for n={n} with search type {search_type}")
    nets = networks(n)
    spd = {}
    for vertex, nets in nets.items():
        results = []
        for net in tqdm(nets, f"Calculatin Sep. Degree for vertex {vertex}"):
            results.append(
                net.get_separation_degree(search_type=search_type)
            )
        spd[vertex] = results
    
    print(spd)