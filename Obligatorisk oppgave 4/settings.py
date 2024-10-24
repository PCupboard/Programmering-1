# Various variables to be used in the game
card_rank = 0
card_suit = 0

# Color variables
red_color = "\033[31m" # Red Color
white_color = "\033[39m" # White/Default Color
blue_color = "\033[34m" # Blue Color

# Miscellaneous
up_line = "\033[A" # Makes the terminal go up one line

# Drawing symbols for a card
hearts = '\u2665'
diamonds = '\u2666'
clubs = '\u2663'
spades = '\u2660'
top_left_corner = "\u250C"
top_right_corner = "\u2510"
horizontal_line = "\u2500"
vertical_line = "\u2502"
bottom_left_corner = "\u2514"
bottom_right_corner = "\u2518"

# A new card design
double_top_left_corner = "\u2554"
double_top_right_corner = "\u2557"
double_horizontal_line = "\u2550"
double_bottom_left_corner = "\u255A"
double_bottom_right_corner = "\u255D"
double_vertical_line = "\u2551"

# Drawing card
playing_card_map = [ [top_left_corner,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       top_right_corner],

                      [vertical_line, card_rank, 0, 0, 0, 0, 0, 0, 0, card_rank, vertical_line],
                      [vertical_line, card_suit, 0, 0, 0, 0, 0, 0, 0, card_suit, vertical_line],
                      [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                      [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                      [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                      [vertical_line, card_suit, 0, 0, 0, 0, 0, 0, 0, card_suit, vertical_line],
                      [vertical_line, card_rank, 0, 0, 0, 0, 0, 0, 0, card_rank, vertical_line],

                      [bottom_left_corner,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       bottom_right_corner] ]
