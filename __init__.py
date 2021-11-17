# -*- coding: utf-8 -*-

import random
import re
from pathlib import Path
from typing import List, Optional, Tuple

import albert

__doc__ = """
Roll any number of dice using the format _d_.

Synopsis: <amount>d<sides> [<amount>d<sides> ...]

Example: "2d6 3d8 1d20"
"""
__title__ = "Dice Roll"
__version__ = "0.0.1"
__authors__ = "Jonah Lawrence"

single_dice_regex = re.compile(r"(\d+)d(\d+)", re.I)

multiple_dice_regex = re.compile(r"(?:(\d+)d(\d+)(?:\D+|$))+", re.I)


def get_icon_path(num_sides: Optional[int]) -> str:
    """
    Get the path to the icon for a die with num_sides sides.

    Args:
        num_sides (Optional[int]): Number of sides on the die or None for the overall total.

    Returns:
        str: The path to the icon.
    """
    icons_path = Path(__file__).parent / "icons"
    # get the icon for the number of sides or d20 if there is no icon for that number
    icon = f"d{num_sides}" if Path(icons_path / f"d{num_sides}.svg").exists() else "d20"
    # use the overall total icon if the number of sides is None
    if num_sides is None:
        icon = "dice"
    # return the path to the icon
    return str(icons_path / f"{icon}.svg")


def roll_dice(num_dice: int, num_sides: int) -> Tuple[int, List[int]]:
    """
    Roll multiple dice with num_sides sides.

    Args:
        num_dice (int): Number of dice to roll.
        num_sides (int): Number of sides on each die.

    Returns:
        Tuple[int, List[int]]: The total and a list of the rolls.
    """
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return sum(rolls), rolls


def get_item_from_rolls(
    rolls: List[int],
    sum_rolls: int,
    num_sides: Optional[int] = None,
) -> albert.Item:
    """
    Creates an Albert Item from a list of rolls, the total, and the number of sides.
    If num_sides is not provided, an "Overall Total" summary item is created.

    Args:
        rolls (List[int]): List of rolls.
        sum_rolls (int): Total of all rolls.
        num_sides (Optional[int]): Number of sides on each die.

    Returns:
        albert.Item: The item to be added to the list of results.
    """
    return albert.Item(
        id=__title__,
        icon=get_icon_path(num_sides),
        text=(
            f"Rolled {len(rolls)}d{num_sides} - Total: {sum_rolls}"
            if num_sides
            else f"Overall Total: {sum_rolls}"
        ),
        subtext=f"Rolls: {', '.join(map(str, rolls))}",
        actions=[
            albert.ClipAction("Copy total to clipboard", str(sum_rolls)),
            albert.ClipAction("Copy rolls to clipboard", ", ".join(map(str, rolls))),
        ],
    )


def get_items(query_string: str) -> List[albert.Item]:
    """
    Convert a query string of dice rolls into a list of Albert Items.

    Args:
        query_string (str): The query string to be parsed.

    Returns:
        List[albert.Item]: The list of items to display.
    """
    results = []
    sum_all_rolls = 0
    all_rolls = []
    # get (num_dice, num_sides) pairs from query string
    matches = single_dice_regex.findall(query_string)
    # roll each pair
    for match in matches:
        num_dice, num_sides = int(match[0]), int(match[1])
        # get random numbers from 1 to num_sides for each die
        sum_rolls, rolls = roll_dice(num_dice, num_sides)
        # add rolls and total to aggregators
        sum_all_rolls += sum_rolls
        all_rolls.extend(rolls)
        # create item for the dice rolls
        results.append(get_item_from_rolls(rolls, sum_rolls, num_sides))
    # if there are multiple dice types, add a summary item
    if len(matches) > 1:
        results.append(get_item_from_rolls(all_rolls, sum_all_rolls))
    return results


def handleQuery(query: albert.Query) -> List[albert.Item]:
    """
    Handler for a query received from Albert.
    """
    query_string = query.string.strip()
    if multiple_dice_regex.fullmatch(query_string):
        try:
            return get_items(query_string)
        except Exception as e:
            albert.warn(e)
            albert.info(
                "Something went wrong. Make sure you're using the correct format."
            )
