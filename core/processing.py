from pythontestlib.strings import format

def process() -> str:
    return format.skip_indentation("""
    This is a text
    """)