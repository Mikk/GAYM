__author__ = 'Mikk'

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)

## Mehike
liigubvasemale1 = "jookseb_vasakule_1.png"
liigubvasemale2 = "jookseb_vasakule_2.png"
liigubparemale1 = "jookseb_paremale_1.png"
liigubparemale2 = "jookseb_paremale_2.png"
hüppabparemale1 = "hüppab_paremale_1.png"
hüppabvasakule1 = "hüppab_vasakule_1.png"
seisab = "seisab.png"

##tiles and stuff
gray_brick = "block64.png"
grass_block = "texture_grass1.jpg"
grass_block_ground = "texture_grass2.jpg"


#platvormi võimalikud pealmised ruudud
OBSTACLE_1 = [(0,0)]
"""
X
"""

OBSTACLE_2 = [(0,0),(64,0)]
"""
XX
"""

OBSTACLE_3 = [(0,0), (64, 0), (64, -64)]
"""
 X
XX
"""

OBSTACLE_4 = [(0,0), (64, 0), (64, -64), (128, -64), (128, 0), (192, 0)]
"""
 XX
XXXX
"""

OBSTACLE_5 = [(0,0), (64, 0), (128, 0), (64, -64), (128, -64), (128, -128)]
"""
  X
 XX
XXX
"""

OBSTACLE_6 = [(0,0), (64,0), (128, 0), (192, 0), (256, 0)]
"""
XXXX
"""

OBSTACLES = [OBSTACLE_1, OBSTACLE_2, OBSTACLE_3, OBSTACLE_4, OBSTACLE_5, OBSTACLE_6]
