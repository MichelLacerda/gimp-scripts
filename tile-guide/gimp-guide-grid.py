#!/usr/bin/python

from gimpfu import *

def gimp_guide_grid(*args):
    image, layer, guide_space_w, guide_space_h, clear = args
    w = image.width
    h = image.height
    if not clear:
        if guide_space_w:
            for x in range(0, w + 1):
                if x % guide_space_w == 0:
                    pdb.gimp_image_add_vguide(image, x)

        if guide_space_h:
            for y in range(0, h + 1):
                if y % guide_space_h == 0:
                    pdb.gimp_image_add_hguide(image, y)
    else:
        pdb.script_fu_guides_remove(image, layer)

register(
    "python_fu_guide_grid",
    "For generate Guide in Grid",
    "Define Space WIDTH and Space HEIGHT or 0(ZERO) to not add Guide",
    "Michel Lacerda",
    "Michel Lacerda - https://github.com/MichelLacerda/gimp-scripts",
    "2015",
    "<Image>/Game/Generate Guides",
    "RGB*, GRAY*",
    [
        (PF_INT, "guide_space_w", "Guide space WIDTH ", 8),
        (PF_INT, "guide_space_h", "Guide space HEIGHT", 8),
        (PF_TOGGLE, "clear",   "Clear", False)
    ],
    [],
    gimp_guide_grid
)

main()