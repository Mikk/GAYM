DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

BLACK = (0,0,0)
WHITE = (255,255,255)
green = (0,200,0)
red = (200,0,0)
white = (255,255,255)
black = (0,0,0)
bright_green = (0,255,0)
bright_red = (255,0,0)

## IMAGES
seisab = "seisab.png"
liigubvasemale1 = "jookseb_vasakule_1.png"
liigubvasemale2 = "jookseb_vasakule_2.png"
liigubvasemale3 = "jookseb_vasakule_3.png"
liigubparemale1 = "jookseb_paremale_1.png"
liigubparemale2 = "jookseb_paremale_2.png"
liigubparemale3 = "jookseb_paremale_3.png"   
hüppabparemale1 = "hüppab_paremale_1.png"
hüppabvasakule1 = "hüppab_vasakule_1.png"
mollingusse_p = "mollingusse_paremale.png"
mollingusse_v = "mollingusse_vasakule.png"
jalaga_p = "jalaga_paremalt.png"
jalaga_v = "jalaga_vasakult.png"
beebiparemale1 = "beebi_paremale1.png"
beebiparemale2 = "beebi_paremale2.png"
beebiparemale3 = "beebi_paremale3.png"
beebivasemale1 = "beebi_vasakule1.png"
beebivasemale2 = "beebi_vasakule2.png"
beebivasemale3 = "beebi_vasakule3.png"
tulnukasparemale1 = "tulnukas_paremale1.png"
tulnukasparemale2 = "tulnukas_paremale2.png"
tulnukasparemale3 = "tulnukas_paremale3.png"
tulnukasvasemale1 = "tulnukas_vasakule1.png"
tulnukasvasemale2 = "tulnukas_vasakule2.png"
tulnukasvasemale3 = "tulnukas_vasakule3.png"
taust1 = "background1.png"
taust2 = "background2.png"
taust3 = "background3.png"


##tiles and stuff
gray_brick = "texture_grass_uus.jpg"


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
