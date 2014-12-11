

#VARIABLES
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


## DIRECTIONS
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

## GAME DATA VARIABLES
GRAVITY = 10

## IMAGES
seisab = "seisab.png"
liigubvasemale1 = "jookseb_vasakule_1.png"
liigubvasemale2 = "jookseb_vasakule_2.png"
liigubvasemale3 = "jookseb_vasakule_3.png"
liigubparemale1 = "jookseb_paremale_1.png"
liigubparemale2 = "jookseb_paremale_2.png"
liigubparemale3 = "jookseb_paremale_3.png"   
hyppabparemale = "hyppab_paremale.png"
hyppabvasakule = "hyppab_vasakule.png"
mollingusse_paremale1 = "mollingusse_paremale1.png"
mollingusse_paremale2 = "mollingusse_paremale2.png"
mollingusse_paremale3 = "mollingusse_paremale3.png"
mollingusse_vasakule1 = "mollingusse_vasakule1.png"
mollingusse_vasakule2 = "mollingusse_vasakule2.png"
mollingusse_vasakule3 = "mollingusse_vasakule3.png"
mollingusse_paremale = [mollingusse_paremale1, mollingusse_paremale2, mollingusse_paremale3]
mollingusse_vasakule = [mollingusse_vasakule1, mollingusse_vasakule2, mollingusse_vasakule3]
mollingusse = {"RIGHT": mollingusse_paremale, "LEFT": mollingusse_vasakule}
jalaga_mollingusse_paremale = "jalaga_paremalt.png"
jalaga_mollingusse_vasakule = "jalaga_vasakult.png"
mehike_liigub_vasemale = [liigubvasemale1, liigubvasemale2, liigubvasemale3]
mehike_liigub_paremale = [liigubparemale1, liigubparemale2, liigubparemale3]
mehike_hyppab_paremale = [hyppabparemale]
mehike_hyppab_vasemale = [hyppabvasakule]
mehike_seisab = [seisab]
mehike_jookseb = {"LEFT": mehike_liigub_vasemale, "RIGHT": mehike_liigub_paremale, "DOWN": mehike_seisab, "UP": mehike_seisab}
mehike_hyppab = {"LEFT": mehike_hyppab_vasemale, "RIGHT": mehike_hyppab_paremale, "DOWN": mehike_seisab, "UP": mehike_seisab}
beebiparemale1 = "beebi_paremale1.png"
beebiparemale2 = "beebi_paremale2.png"
beebiparemale3 = "beebi_paremale3.png"
beebivasemale1 = "beebi_vasakule1.png"
beebivasemale2 = "beebi_vasakule2.png"
beebivasemale3 = "beebi_vasakule3.png"
beebi_seisab = [beebivasemale2]
beebi_liigub_paremale = [beebiparemale1, beebiparemale2, beebiparemale3]
beebi_liigub_vasakule = [beebivasemale1, beebivasemale2, beebivasemale3]
beebi_jookseb = {LEFT: beebi_liigub_vasakule, RIGHT: beebi_liigub_paremale, UP: beebi_seisab, DOWN: beebi_seisab}
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
