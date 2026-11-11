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

    #Tier 2
    radiant = Node("Radiant", 120, 685, "#fcdf91", "#d3bc7e", tier = 2, parents = [light, fire]) #lightning/storm?
    sound = Node("Sound", 240, 685, "#cebdb0", "#a89f98", tier = 2, parents = [light, air])
    crystal = Node("Crystal", 360, 685, "#7f87f7", "#747ace", tier = 2, parents = [light, earth]) #nature if life?
    ice = Node("Ice", 480, 685, "#bddbfa", "#99bde0", tier = 2, parents = [light, water])
    smoke = Node("Smoke", 600, 685, "#b7b7b7", "#9c9c9c", tier = 2, parents = [fire, air])
    magma = Node("Magma", 720, 685, "#ca7344", "#aa7153", tier = 2, parents = [fire, earth]) #
    steam = Node("Steam", 840, 685, "#d6e1f2", "#abb4c2", tier = 2, parents = [fire, water])
    dust = Node("Dust", 1080, 685, "#e2c84b", "#b4a245", tier = 2, parents = [air, earth])
    cloud = Node("Cloud", 1200, 685, "#efefef", "#bebebe", tier = 2, parents = [air, water]) # storm/lightning,
    mud = Node("Mud", 1320, 685, "#6a4214", "#5e3e1a", tier = 2, parents = [earth, water]) # nature,
    ash = Node("Ash", 1440, 685, "#413C3C", "#5F5555", tier = 2, parents = [dark, fire]) #decay? 
    miasma = Node("Miasma", 1560, 685, "#3C4436", "#56634D", tier = 2, parents = [dark, air]) #decay?
    metal = Node("Metal", 1680, 685, "#a5a5a5ff", "#83807dff", tier = 2, parents = [dark, earth])
    blood = Node("Blood", 1800, 685, "#a50909", "#b12121", tier = 2, parents = [dark, water]) #nature if blood?
    shadow = Node("Shadow", 960, 685, "#2B2727FF", "#524C4CFF", tier = 2, parents = [dark, light])

    #Tier 3
    decay = Node("(Decay)", 795, 510, "#929b7c", "#707562", tier = 3, parents = [ash, miasma])
    storm = Node("(Storm)", 905, 510, "#5964f9", "#626ad4", tier = 3, parents = [radiant, cloud])
    nature = Node("(Nature)", 1125, 510, "#4f7827", "#62883c", tier = 3, parents = [crystal, mud, blood])

    #Make list to draw
    nodes = [pure, fire, air, earth, water, light, dark, 
             radiant, sound, crystal, ice, smoke, magma, steam, dust, cloud, mud, ash, miasma, metal, blood, shadow, 
             decay, storm, nature]
    return nodes


def draw_nodes(nodes:list[Node], screen: pygame.Surface):
    for node in nodes:
        node.draw_lines(screen)
    for node in nodes:
        node.draw(screen)


def pure_increment(pure: PureNode, active_nodes: list[Node]):
    targets = [n for n in active_nodes if n.type != ClickType.PURE]

    for node in targets:
        if node.value <= pure.value:
            return 1

    for node in targets:
        node.value -= pure.value

    pure.value += 1
    return 0


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

