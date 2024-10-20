hearts = '♥'
diamonds = '♦'
clubs = '♣'
spades = '♠'

# Drawing symbols for a card
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



# 0 = blank space
# 1 = horizontal_line
# 2 = top_left_corner
# 3 = top_right_corner
# 4 = vertical_line
# 5 = bottom_left_corner
# 6 = bottom_right_corner

card_suit = clubs
card_num = "Q"


def draw_playing_card(card_type, card_number):
    print("\u250C" + "\u2500" * 9 + "\u2510")
    for row in range(5):
        print("\u2502" + " " * 9 + "\u2502")
    print("\u2514" + "\u2500" * 9 + "\u2518")


#draw_playing_card(hearts, card_num)

playing_card_map = [ [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
                     [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                     [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                     [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                     [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                     [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                     [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6] ]

playing_card_map2 = [ [top_left_corner,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       top_right_corner],

                      [vertical_line, card_num, 0, 0, 0, 0, 0, 0, 0, card_num, vertical_line],
                      [vertical_line, card_suit, 0, 0, 0, 0, 0, 0, 0, card_suit, vertical_line],
                      [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                      [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                      [vertical_line, 0, 0, 0, 0, 0, 0, 0, 0, 0, vertical_line],
                      [vertical_line, card_suit, 0, 0, 0, 0, 0, 0, 0, card_suit, vertical_line],
                      [vertical_line, card_num, 0, 0, 0, 0, 0, 0, 0, card_num, vertical_line],

                      [bottom_left_corner,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       bottom_right_corner], ]

playing_card_map3 = [ [top_left_corner,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       top_right_corner],

                      [vertical_line, card_num, 0, 0, 0, 0, 0, 0, 0, card_num, vertical_line],
                      [vertical_line, card_suit, 0, 0, 0, 0, 0, 0, 0, card_suit, vertical_line],
                      [vertical_line, 0, 0, 0, "\u2571", "\u2502", 0, 0, 0, 0, vertical_line],
                      [vertical_line, 0, 0, 0, "\u2500", "\u253C", "\u2500", 0, 0, 0, vertical_line],
                      [vertical_line, 0, 0, 0, 0, "\u2502", 0, 0, 0, 0, vertical_line],
                      [vertical_line, card_suit, 0, 0, 0, 0, 0, 0, 0, card_suit, vertical_line],
                      [vertical_line, card_num, 0, 0, 0, 0, 0, 0, 0, card_num, vertical_line],

                      [bottom_left_corner,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       horizontal_line, horizontal_line, horizontal_line,
                       bottom_right_corner], ]

for row in playing_card_map3:
    for element in row:
        if element != 0:
            print(element, end='')
        else:
            print(" ", end='')
    print()

print("\u1F0A3")
bruker = input("")