#DIGM 131 - Assignment 3: Function Library Main Scene

import maya.cmds as cmds
import scene_functions as sf

# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Create a ground plane.
ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]

# ---------------------------------------------------------------------------
# Build Scene
# ---------------------------------------------------------------------------

# --- Buildings ---
# Create a few buildings with different sizes and positions
sf.create_building(width=6, height=12, depth=6, position=(-12, 0, 10))
sf.create_building(width=4, height=8, depth=4, position=(-6, 0, 10))
sf.create_building(width=5, height=10, depth=5, position=(-9, 0, 5))

# --- Trees ---
# Create some trees
sf.create_tree(position=(5, 0, -5))
sf.create_tree(position=(8, 0, -6))

# Use place_in_circle to create a circular park of trees
sf.place_in_circle(
    sf.create_tree,
    count=8,
    radius=10,
    center=(10, 0, 10)
)

# --- Fence ---
sf.create_fence(length=12, height=1.5, post_count=6, position=(4, 0, 8))

# --- Lamp posts ---
sf.create_lamp_post(position=(0, 0, 0))
sf.create_lamp_post(position=(3, 0, 3))
sf.create_lamp_post(position=(-3, 0, 3))
sf.create_lamp_post(position=(0, 0, 6))

# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
