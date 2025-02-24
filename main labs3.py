from abc import ABC, abstractmethod

class Equipment(ABC):
    total_equipment = 0

    def __init__(self):
        Equipment.total_equipment += 1

    @staticmethod
    def get_total_equipment():
        return Equipment.total_equipment

    @abstractmethod
    def __str__(self):
        pass

    def format_info(self):
        return str(self).replace(", ", "\n")

    def __eq__(self, other):
        return self.name == other.name and self.gender == other.gender

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return f"{self.name} + {other.name}"

    def __hash__(self):
        return hash((self.name, self.gender))


class User:
    def __init__(self, name, age, gender, skill, height, weight, clothing_size, leg_size, fasteners_size, helmet_size):
        self.name = name
        self.age = age
        self.gender = gender
        self.skill = skill
        self.height = height
        self.weight = weight
        self.clothing_size = clothing_size
        self.leg_size = leg_size
        self.fasteners = fasteners_size
        self.helmet_size = helmet_size

    def __str__(self):
        return (f"User(Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Skill: {self.skill}, "
                f"Height: {self.height}, Weight: {self.weight}, Clothing Size: {self.clothing_size}, "
                f"Leg Size: {self.leg_size}, Fasteners Size: {self.fasteners}, Helmet Size: {self.helmet_size})")

    @classmethod
    def from_input(cls):
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            skill = input("Enter skill level (beginner, intermediate, advanced): ")
            height = float(input("Enter height (in cm): "))
            weight = float(input("Enter weight (in kg): "))
            clothing_size = input("Enter clothing size: ")
            leg_size = float(input("Enter leg size (in cm): "))
            fasteners_size = input("Enter fasteners size: ")
            helmet_size = input("Enter helmet size: ")
            return cls(name, age, gender, skill, height, weight, clothing_size, leg_size, fasteners_size, helmet_size)
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None

    def update_skill(self, new_skill):
        self.skill = new_skill
        print(f"Skill updated to: {self.skill}")


class Board(Equipment):
    def __init__(self, name, gender, skill, height):
        super().__init__()
        self.name = name
        self.gender = gender
        self.skill = skill
        self.height = height

    def __str__(self):
        return f"Board(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill}, Height: {self.height})"

    @classmethod
    def from_input(cls):
        name = input("Enter board name: ")
        gender = input("Enter gender: ")
        skill = input("Enter skill level (beginner, intermediate, advanced): ")
        height = float(input("Enter recommended height (in cm): "))
        return cls(name, gender, skill, height)


class Boots(Equipment):
    def __init__(self, name, gender, skill, leg_size):
        super().__init__()
        self.name = name
        self.gender = gender
        self.skill = skill
        self.leg_size = leg_size

    def __str__(self):
        return f"Boots(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill}, Leg Size: {self.leg_size})"

    @classmethod
    def from_input(cls):
        name = input("Enter boots name: ")
        gender = input("Enter gender: ")
        skill = input("Enter skill level (beginner, intermediate, advanced): ")
        leg_size = float(input("Enter leg size (in cm): "))
        return cls(name, gender, skill, leg_size)


class Fasteners(Equipment):
    def __init__(self, name, gender, skill, fasteners_size):
        super().__init__()
        self.name = name
        self.gender = gender
        self.skill = skill
        self.fasteners = fasteners_size

    def __str__(self):
        return f"Fasteners(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill}, Fasteners Size: {self.fasteners})"

    @classmethod
    def from_input(cls):
        name = input("Enter fasteners name: ")
        gender = input("Enter gender: ")
        skill = input("Enter skill level (beginner, intermediate, advanced): ")
        fasteners_size = input("Enter fasteners size: ")
        return cls(name, gender, skill, fasteners_size)


class Helmet(Equipment):
    def __init__(self, name, gender, helmet_size):
        super().__init__()
        self.name = name
        self.gender = gender
        self.size = helmet_size

    def __str__(self):
        return f"Helmet(Name: {self.name}, Gender: {self.gender}, Size: {self.size})"

    @classmethod
    def from_input(cls):
        name = input("Enter helmet name: ")
        gender = input("Enter gender: ")
        helmet_size = input("Enter helmet size: ")
        return cls(name, gender, helmet_size)


def recommend_board(user, boards):
    for board in boards:
        if (board.gender == user.gender and
            board.skill == user.skill and
            board.height >= user.height - 10 and
            board.height <= user.height + 10):
            return board
    return None


def recommend_boots(user, boots):
    for boot in boots:
        if (boot.gender == user.gender and
            boot.skill == user.skill and
            boot.leg_size == user.leg_size):
            return boot
    return None


def recommend_fasteners(user, fasteners):
    for fastener in fasteners:
        if (fastener.gender == user.gender and
            fastener.skill == user.skill and
            fastener.fasteners == user.fasteners):
            return fastener
    return None


def recommend_helmet(user, helmets):
    for helmet in helmets:
        if (helmet.gender == user.gender and
            helmet.size == user.helmet_size):
            return helmet
    return None


def edit_user_info(user):
    while True:
        print("\nCurrent user information:")
        print(user)
        print("\nSelect field to edit:")
        print("1. Name")
        print("2. Age")
        print("3. Gender")
        print("4. Skill")
        print("5. Height")
        print("6. Weight")
        print("7. Clothing Size")
        print("8. Leg Size")
        print("9. Fasteners Size")
        print("10. Helmet Size")
        print("11. Return to main menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            user.name = input("Enter new name: ")
        elif choice == "2":
            try:
                user.age = int(input("Enter new age: "))
            except ValueError:
                print("Invalid input. Age must be a number.")
        elif choice == "3":
            user.gender = input("Enter new gender: ")
        elif choice == "4":
            user.skill = input("Enter new skill level (beginner, intermediate, advanced): ")
        elif choice == "5":
            try:
                user.height = float(input("Enter new height (in cm): "))
            except ValueError:
                print("Invalid input. Height must be a number.")
        elif choice == "6":
            try:
                user.weight = float(input("Enter new weight (in kg): "))
            except ValueError:
                print("Invalid input. Weight must be a number.")
        elif choice == "7":
            user.clothing_size = input("Enter new clothing size: ")
        elif choice == "8":
            try:
                user.leg_size = float(input("Enter new leg size (in cm): "))
            except ValueError:
                print("Invalid input. Leg size must be a number.")
        elif choice == "9":
            user.fasteners = input("Enter new fasteners size: ")
        elif choice == "10":
            user.helmet_size = input("Enter new helmet size: ")
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

    return user


def interactive_menu(user, boards, boots, fasteners, helmets):
    while True:
        print("\n1. Add a new board")
        print("2. Add new boots")
        print("3. Add new fasteners")
        print("4. Add a new helmet")
        print("5. Recommend equipment")
        print("6. Edit user information")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAdding a new board:")
            new_board = Board.from_input()
            if new_board:
                boards.add(new_board)
                print("\nNew board added:")
                print(new_board)
        elif choice == "2":
            print("\nAdding new boots:")
            new_boots = Boots.from_input()
            if new_boots:
                boots.add(new_boots)
                print("\nNew boots added:")
                print(new_boots)
        elif choice == "3":
            print("\nAdding new fasteners:")
            new_fasteners = Fasteners.from_input()
            if new_fasteners:
                fasteners.add(new_fasteners)
                print("\nNew fasteners added:")
                print(new_fasteners)
        elif choice == "4":
            print("\nAdding a new helmet:")
            new_helmet = Helmet.from_input()
            if new_helmet:
                helmets.add(new_helmet)
                print("\nNew helmet added:")
                print(new_helmet)
        elif choice == "5":
            recommended_board = recommend_board(user, boards)
            if recommended_board:
                print("\nRecommended Board:")
                print(recommended_board.format_info())
            else:
                print("\nNo suitable board found.")

            recommended_boots = recommend_boots(user, boots)
            if recommended_boots:
                print("\nRecommended Boots:")
                print(recommended_boots.format_info())
            else:
                print("\nNo suitable boots found.")

            recommended_fasteners = recommend_fasteners(user, fasteners)
            if recommended_fasteners:
                print("\nRecommended Fasteners:")
                print(recommended_fasteners.format_info())
            else:
                print("\nNo suitable fasteners found.")

            recommended_helmet = recommend_helmet(user, helmets)
            if recommended_helmet:
                print("\nRecommended Helmet:")
                print(recommended_helmet.format_info())
            else:
                print("\nNo suitable helmet found.")
        elif choice == "6":
            print("\nEditing user information:")
            user = edit_user_info(user)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    user = User.from_input()
    if not user:
        return

    boards = set()
    boots = set()
    fasteners = set()
    helmets = set()

    boards.add(Board("Board1", "male", "intermediate", 170))
    boards.add(Board("Board2", "female", "beginner", 160))
    boards.add(Board("Board3", "male", "advanced", 180))

    boots.add(Boots("Boots1", "male", "intermediate", 42))
    boots.add(Boots("Boots2", "female", "beginner", 38))
    boots.add(Boots("Boots3", "male", "advanced", 44))

    fasteners.add(Fasteners("Fasteners1", "male", "intermediate", "M"))
    fasteners.add(Fasteners("Fasteners2", "female", "beginner", "S"))
    fasteners.add(Fasteners("Fasteners3", "male", "advanced", "L"))

    helmets.add(Helmet("Helmet1", "male", "L"))
    helmets.add(Helmet("Helmet2", "female", "M"))
    helmets.add(Helmet("Helmet3", "male", "XL"))

    print(f"\nTotal equipment created: {Equipment.get_total_equipment()}")

    board = Board("Board1", "male", "intermediate", 170)
    print("\nBoard object:")
    print(board)

    print(f"\nTotal boards: {len(boards)}")

    print("\nFormatted board info:")
    print(board.format_info())

    board1 = Board("Board1", "male", "intermediate", 170)
    board2 = Board("Board2", "female", "beginner", 160)
    print(f"\nOperator overloading demo: {board1 != board2}")

    print("\nUpdating user skill:")
    user.update_skill("advanced")

    interactive_menu(user, boards, boots, fasteners, helmets)


if __name__ == "__main__":
    main()