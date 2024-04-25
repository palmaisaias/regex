import re
import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", 
         "Jordan Alexander Williams", "Madonna", "programming is cool"]


def verify_name(names):
    print()
    for name in names:
        name_match = re.match(r"([A-Z][A-Za-z]+)( [A-Z][a-z]*|[A-Z])? ([A-Z]'?[A-Za-z-]+)", name)
        #---Including middle initial or name: 
        #--- 1. Note there is no space between the FN grouping and MN grouping parenthesis ')('
        #--- rather the space is found inside the grouping of the MD option. This is to assure that the 'match' for the 
        #--- MD (if it exists) is IMMEDIATELY after the FN match. The space must then be included withing the MD grouping.
        #--- 2. Pipe allows match for MD grouping to either allow a title case MD OR a single, uppercase middle initial
        #--- 3. the space after the '?' attached to the MD is super important because SINCE the MD match is optional, IF a name in the list
        #--- did not have a middle intial, re.match expectation would be another set of letters starting with an upper and starting immediately
        #--- without a space. Albeit the spaces were/ARE tough to understand.
        #--- ALSO. groupings are needed if we want to affect different parts of a string. A group for every part of the string I need/want
        #--- to interract with. So, not just for aesthetics lol
        if name_match:
            print(name_match.group())
        else:
            print(Style.DIM + Fore.RED + 'Invalid Name')
    print()

verify_name(names)