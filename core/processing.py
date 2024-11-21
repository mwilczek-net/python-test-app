# from pythontestlib.strings import format
from numlib import converters

# def process() -> str:
#     return format.skip_indentation("""
#     This is a text
#     """)

def number_list() -> list[int]:
    return [converters.opposit(x) for x in range(11)]