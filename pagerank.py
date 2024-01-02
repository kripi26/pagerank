class WebGraph:
    def __init__(self):
        self.graph = {}
        self.damping_factor = 0.85    #Usually this is the factor 
        self.epsilon = 1e-6

    def add_page(self, page, outgoing_links):
        self.graph[page] = outgoing_links

    def page_rank(self, num_iterations=10):
        num_pages = len(self.graph)
        ranks = {page: 1 / num_pages for page in self.graph}

        for _ in range(num_iterations):
            new_ranks = {}
            for page in self.graph:
                incoming_pages = [p for p, links in self.graph.items() if page in links]
                rank = (1 - self.damping_factor) / num_pages

                for incoming_page in incoming_pages:
                    rank += self.damping_factor * ranks[incoming_page] / len(self.graph[incoming_page])

                new_ranks[page] = rank

            if all(abs(new_ranks[page] - ranks[page]) < self.epsilon for page in self.graph):
                break

            ranks = new_ranks

        return ranks


web_graph = WebGraph()

web_graph.add_page('A', ['B', 'C','D'])
web_graph.add_page('B', ['C','D'])
web_graph.add_page('C', ['A','D'])
web_graph.add_page('D',['A','B', 'C'])
ranks = web_graph.page_rank()
sorted_ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)   #To Sort the Dictionary

print("PageRank Results:")
for page, rank in sorted_ranks:
    print(f"{page}: {rank}")
