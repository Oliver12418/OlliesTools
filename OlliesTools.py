class OlliesTools:

    @staticmethod
    def repchar(lst1: list[str], x: int, y: int, char: str) -> list[str]:
        """
        This function replaces a character at a given x, y coordinate with the provided character.

        Args:
            lst1 (list[str]): The list of strings to be modified.
            x (int): The x-coordinate of the character to be replaced.
            y (int): The y-coordinate of the character to be replaced.
            char (str): The character to replace the existing character with.

        Returns:
            list[str]: The modified list of strings.
        """

        lst2=lst1[:]
        a=list(lst2[y])
        a[x]=char
        lst2[y]=''.join(a)
        return(lst2)

    @staticmethod
    def IsEven(number):
        """
        This function returns True if the number is even, and False if the number is odd.

        Args:
            number (int): The number to be checked.

        Returns:
            bool: True if the number is even, False if the number is odd.
        """

        return number%2==0
    
    @staticmethod
    def TextFormatting(TextFormatting: int, TextColor: int, BackgroundColor: int, Text: str):
        """
        Syntax: Text format, Text color, Background color, Text

        Color formatting: \033[Format;Color;Back Text

        The numbers for the formatting are listed below.

        Formats:
        0: Regular
        1: Bold
        2: Low Intensity
        3: Italic
        4: Underline
        5: Blinking
        6: Reverse
        7: Background
        8: Invisible
        
        Text Color:
        30: Black
        31: Red
        32: Green
        34: Blue
        35: Magenta
        36: Cyan
        37: White

        Background Color:
        40: Black
        41: Red
        42: Green
        43: Yellow
        44: Blue
        45: Magenta
        46: Cyan
        47: White
        """

        string="\033["+";".join([str(TextFormatting), str(TextColor), str(BackgroundColor)])+"m"+Text+"\033[0m"
        return string
