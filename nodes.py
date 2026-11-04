import pygame
from clickables import *

def create_nodes() -> list[Node]:
    fire = Node("Fire", 445, 500, "#ff9900", "#da9124")
    air = Node("Air", 575, 500, "#f3f3f3", "#cacaca")
    earth = Node("Earth", 705, 500, "#7f6000", "#644e0b")
    water = Node("Water", 835, 500, "#003cff", "#3030e4")
    pure = PureNode("Pure Magic", 640, 630, "#8a00f8", "#9d37f1")
    test = Node("Test", 200, 200, "gray", "white", False)
    nodes = [pure, fire, air, earth, water, test]
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
    if len(node.parents) > 0:
        sufficient_ct = 0
        for parent in node.parents:
            if parent.value <= pure.value:
                return
            else:
                sufficient_ct += 1
        if sufficient_ct == len(node.parents):
            for parent in node.parents:
                parent.value -= pure.value
    if node.active == True:
        node.value += pure.value

