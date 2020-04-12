#from lxml import html
import networkx as nx
from lxml import html
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests


def traverse(parent, graph, labels):
    labels[hash(parent)] = parent.name
    for node in parent.children:
        if isinstance(node, NavigableString):
            continue
        graph.add_edge(hash(parent), hash(node))
        traverse(node, graph, labels)

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1"
req = requests.get(url)
raw = req.content
# print(raw)


G = nx.DiGraph()
labels = {}
#html_tag = html.document_fromstring(raw)
soup = BeautifulSoup(raw, 'html.parser')
print(soup.children)
# html_tag = next(soup.children)

# # print(html_tag)
# traverse(html_tag, G, labels)

# pos = graphviz_layout(G, prog='dot')

# label_props = {'size': 16,
#                'color': 'black',
#                'weight': 'bold',
#                'horizontalalignment': 'center',
#                'verticalalignment': 'center',
#                'clip_on': True}
# bbox_props = {'boxstyle': "round, pad=0.2",
#               'fc': "grey",
#               'ec': "b",
#               'lw': 1.5}

# nx.draw_networkx_edges(G, pos, arrows=True)
# ax = plt.gca()

# for node, label in labels.items():
#         x, y = pos[node]
#         ax.text(x, y, label,
#                 bbox=bbox_props,
#                 **label_props)

# ax.xaxis.set_visible(False)
# ax.yaxis.set_visible(False)
# plt.show()