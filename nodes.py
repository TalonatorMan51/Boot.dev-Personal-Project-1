import pygame
from clickables import *

def create_nodes() -> list[Node]:
    #Tier 1
    fire = Node("Fire", 765, 860, "#ff9900", "#da9124")
    air = Node("Air", 895, 860, "#f3f3f3", "#cacaca")
    earth = Node("Earth", 1025, 860, "#7f6000", "#644e0b")
    water = Node("Water", 1155, 860, "#003cff", "#3030e4")
    light = Node("Light", 635, 850, "#faf4cf", "#e4dfc4")
    dark = Node("Dark", 1285, 850, "#434343", "#5F5F5F")
    #Pure
    pure = PureNode("Pure Magic", 960, 990, "#8a00f8", "#9d37f1")

    #Tier 2 - Dual Combos
    l1 = Node("[Radiant]", 120, 685, "white", "gray", tier = 2, parents = [light, fire])
    l2 = Node("lightair", 240, 685, "white", "gray", tier = 2, parents = [light, air])
    l3 = Node("[Life]", 360, 685, "white", "gray", tier = 2, parents = [light, earth])
    l4 = Node("[Rainbow/Ice]", 480, 685, "white", "gray", tier = 2, parents = [light, water])
    smoke = Node("Smoke", 600, 685, "#b7b7b7", "#9c9c9c", tier = 2, parents = [fire, air])
    magma = Node("Magma", 720, 685, "#ca7344", "#aa7153", tier = 2, parents = [fire, earth])
    steam = Node("Steam", 840, 685, "#d6e1f2", "#abb4c2", tier = 2, parents = [fire, water])
    dust = Node("Dust", 1080, 685, "#e2c84b", "#b4a245", tier = 2, parents = [air, earth])
    cloud = Node("Cloud", 1200, 685, "#efefef", "#bebebe", tier = 2, parents = [air, water])
    mud = Node("Mud", 1320, 685, "#6a4214", "#5e3e1a", tier = 2, parents = [earth, water])
    d1 = Node("darkfire", 1440, 685, "black", "gray", tier = 2, parents = [dark, fire])
    d2 = Node("[Miasma]", 1560, 685, "black", "gray", tier = 2, parents = [dark, air])
    d3 = Node("darkearth", 1680, 685, "black", "gray", tier = 2, parents = [dark, earth])
    d4 = Node("[Depth/Abyss]", 1800, 685, "black", "gray", tier = 2, parents = [dark, water])
    dl = Node("[Twilight]", 960, 685, "gray", "gray", tier = 2, parents = [dark, light])

    test = Node("Test", 200, 200, "gray", "white", tier = 100, parents = [fire, air, earth, water, light, dark])
    nodes = [pure, fire, air, earth, water, light, dark, l1, l2, l3, l4, smoke, magma, steam, dust, cloud, mud, d1, d2, d3, d4, dl, test]
    return nodes


def draw_nodes(nodes:list[Node], screen: pygame.Surface):
    for node in nodes:
        node.draw(screen)


def pure_increment(pure: PureNode, active_nodes: list[Node]):
    sufficient_ct = 0
    for node in active_nodes:
        if node.type == ClickType.PURE:
            continue
        elif node.value <= pure.value:
            return 1
        else:
            sufficient_ct += 1 
    if sufficient_ct == len(active_nodes) - 1:
        for node in active_nodes:
            if node.type == ClickType.PURE:
                continue
            node.value -= pure.value
    pure.value += 1


def reg_increment(node:Node, pure:PureNode):
    if node.is_unlocked == True:
        allowed = True
    else:
        allowed = False
    if len(node.parents) > 0:
        sufficient_ct = 0
        for parent in node.parents:
            if parent.value <= pure.value:
                return
            elif node.is_unlocked:
                sufficient_ct += 1
        if sufficient_ct == len(node.parents):
            for parent in node.parents:
                parent.value -= pure.value
    if allowed:
        if pure.value <= 1:
            node.value += 1
        else:
            node.value += int((pure.value/node.tier))

