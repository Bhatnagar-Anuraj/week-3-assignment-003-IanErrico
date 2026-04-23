# DIGM 131 - Assignment 3: Function Library Scene Functions

import maya.cmds as cmds
import math


def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    """Create a simple building from a cube, placed on the ground plane.

    The building is a single scaled cube whose base sits at ground level
    (y = 0) at the given position.

    Args:
        width (float): Width of the building along the X axis.
        height (float): Height of the building along the Y axis.
        depth (float): Depth of the building along the Z axis.
        position (tuple): (x, y, z) ground-level position. The building
            base will rest at this point; y is typically 0.

    Returns:
        str: The name of the created building transform node.
    """
    # Create cube
    building = cmds.polyCube(w=width, h=height, d=depth)[0]

    # Move the cube so its base sits on ground
    x, y, z = position
    cmds.move(x, y + height / 2.0, z, building)

    return building


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2,
                position=(0, 0, 0)):
    """Create a simple tree using a cylinder trunk and a sphere canopy.

    Args:
        trunk_radius (float): Radius of the cylindrical trunk.
        trunk_height (float): Height of the trunk cylinder.
        canopy_radius (float): Radius of the sphere used for the canopy.
        position (tuple): (x, y, z) ground-level position for the tree base.

    Returns:
        str: The name of a group node containing the trunk and canopy.
    """
    # Create trunk
    trunk = cmds.polyCylinder(r=trunk_radius, h=trunk_height)[0]
    cmds.move(0, trunk_height / 2.0, 0, trunk)

    # Create canopy
    canopy = cmds.polySphere(r=canopy_radius)[0]
    cmds.move(0, trunk_height + canopy_radius, 0, canopy)

    # Group trunk and canopy
    tree_group = cmds.group(trunk, canopy, name="tree_group")

    # Move entire tree to position
    x, y, z = position
    cmds.move(x, y, z, tree_group)

    return tree_group


def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a simple fence made of posts and rails.

    The fence runs along the X axis starting at the given position.

    Args:
        length (float): Total length of the fence along the X axis.
        height (float): Height of the fence posts.
        post_count (int): Number of vertical posts (must be >= 2).
        position (tuple): (x, y, z) starting position of the fence.

    Returns:
        str: The name of a group node containing all fence parts.
    """
    # Ensure a valid post count
    if post_count < 2:
        raise ValueError("post_count must be at least 2")

    fence_parts = []

    # Calculate spacing between posts
    spacing = length / (post_count - 1)

    # Create posts
    for i in range(post_count):
        post = cmds.polyCube(w=0.2, h=height, d=0.2)[0]
        cmds.move(i * spacing, height / 2.0, 0, post)
        fence_parts.append(post)

    # Create rail
    rail = cmds.polyCube(w=length, h=0.2, d=0.2)[0]
    cmds.move(length / 2.0, height * 0.75, 0, rail)
    fence_parts.append(rail)

    # Group everything
    fence_group = cmds.group(fence_parts, name="fence_group")

    # Move group to position
    x, y, z = position
    cmds.move(x, y, z, fence_group)

    return fence_group


def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    """Create a street lamp using a cylinder pole and a sphere light.

    Args:
        pole_height (float): Height of the lamp pole.
        light_radius (float): Radius of the sphere representing the light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
        str: The name of a group node containing the pole and light.
    """
    # Create pole
    pole = cmds.polyCylinder(r=0.1, h=pole_height)[0]
    cmds.move(0, pole_height / 2.0, 0, pole)

    # Create light
    light = cmds.polySphere(r=light_radius)[0]
    cmds.move(0, pole_height + light_radius, 0, light)

    # Group both of them
    lamp_group = cmds.group(pole, light, name="lamp_group")

    # Move group to position
    x, y, z = position
    cmds.move(x, y, z, lamp_group)

    return lamp_group


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                     **kwargs):
    """Place objects created by 'create_func' in a circular arrangement.

    This is a higher-order function: it takes another function as an
    argument and calls it repeatedly to place objects around a circle.

    Args:
        create_func (callable): A function from this module (e.g.,
            create_tree) that accepts a 'position' keyword argument
            and returns an object name.
        count (int): Number of objects to place around the circle.
        radius (float): Radius of the circle.
        center (tuple): (x, y, z) center of the circle.
        **kwargs: Additional keyword arguments passed to create_func
            (e.g., trunk_height=4).

    Returns:
        list: A list of object/group names created by create_func.
    """
    results = []

    for i in range(count):
        angle = 2 * math.pi * i / count

        x = center[0] + radius * math.cos(angle)
        z = center[2] + radius * math.sin(angle)
        y = center[1]

        obj = create_func(position=(x, y, z), **kwargs)
        results.append(obj)

    circle_group = cmds.group(results, name="circle_group")

    return results
