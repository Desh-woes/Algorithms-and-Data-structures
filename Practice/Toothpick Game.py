class Toothpick:

    def __init__(self, group, picked=False):
        self.group = group
        self.picked = picked

    def reset(self):
        self.picked = False

    def quit_game(self):
        self.picked = True


class ToothpickGame:

    def __init__(self):
        self.toothpick_list = []

        for x in range(0, 9):
            if x < 3:
                toothpick = Toothpick(1)
            elif x < 6:
                toothpick = Toothpick(2)
            elif x < 9:
                toothpick = Toothpick(3)
            self.toothpick_list.append(toothpick)

    def input_handler(self):
        player1 = 'Pelumi'
        player2 = 'Femi'
        while self.game_in_session():
            print("remove 1, 2, or 3 toothpicks from any group")
            print(self.current_state())

            while True:
                player_1_group = input("Player 1, please select your group: \n")
                if player_1_group not in range(1, 4):
                    print("Sorry, your response was invalid. Please select a number from 1 - 3")
                    continue
                else:
                    # we're happy with the value given.
                    # we're ready to exit the loop.
                    break

            input("Player 1, please select your group: \n")
            input("Player 1, please remove toothpicks")

    def game_in_session(self):
        for x in self.toothpick_list:
            if not x.picked:
                return True
            else:
                return False

    def current_state(self):
        group1 = 0
        group2 = 0
        group3 = 0
        for x in self.toothpick_list:
            if x.group == 1 and not x.picked:
                group1 += 1
            elif x.group == 2 and not x.picked:
                group2 += 1
            elif x.group == 3 and not x.picked:
                group3 += 1
        return "|Group 1: " + str(group1) + "|, |Group 2: " + str(group2) + "|, |Group 3: " + str(group3) + "|"




tooth = ToothpickGame()
print(tooth.toothpick_list)
tooth.input_handler()