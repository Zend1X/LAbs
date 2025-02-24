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


class Board:
    def __init__(self, name, gender, skill, height):
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


class Boots:
    def __init__(self, name, gender, skill, leg_size):
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


class Fasteners:
    def __init__(self, name, gender, skill, fasteners_size):
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


class Helmet:
    def __init__(self, name, gender, helmet_size):
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


# Пример интерактивного меню
def interactive_menu(user, boards, boots, fasteners, helmets):
    while True:
        print("\n1. Add a new board")
        print("2. Add new boots")
        print("3. Add new fasteners")
        print("4. Add a new helmet")
        print("5. Recommend equipment")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAdding a new board:")
            new_board = Board.from_input()
            boards.append(new_board)
            print("\nNew board added:")
            print(new_board)
        elif choice == "2":
            print("\nAdding new boots:")
            new_boots = Boots.from_input()
            boots.append(new_boots)
            print("\nNew boots added:")
            print(new_boots)
        elif choice == "3":
            print("\nAdding new fasteners:")
            new_fasteners = Fasteners.from_input()
            fasteners.append(new_fasteners)
            print("\nNew fasteners added:")
            print(new_fasteners)
        elif choice == "4":
            print("\nAdding a new helmet:")
            new_helmet = Helmet.from_input()
            helmets.append(new_helmet)
            print("\nNew helmet added:")
            print(new_helmet)
        elif choice == "5":
            # Рекомендации оборудования
            recommended_board = recommend_board(user, boards)
            if recommended_board:
                print("\nRecommended Board:")
                print(recommended_board)
            else:
                print("\nNo suitable board found.")

            recommended_boots = recommend_boots(user, boots)
            if recommended_boots:
                print("\nRecommended Boots:")
                print(recommended_boots)
            else:
                print("\nNo suitable boots found.")

            recommended_fasteners = recommend_fasteners(user, fasteners)
            if recommended_fasteners:
                print("\nRecommended Fasteners:")
                print(recommended_fasteners)
            else:
                print("\nNo suitable fasteners found.")

            recommended_helmet = recommend_helmet(user, helmets)
            if recommended_helmet:
                print("\nRecommended Helmet:")
                print(recommended_helmet)
            else:
                print("\nNo suitable helmet found.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Основная функция
def main():
    # Создаем пользователя
    user = User.from_input()

    # Инициализация списков
    boards = [
        Board("Board1", "male", "intermediate", 170),
        Board("Board2", "female", "beginner", 160),
        Board("Board3", "male", "advanced", 180),
    ]

    boots = [
        Boots("Boots1", "male", "intermediate", 42),
        Boots("Boots2", "female", "beginner", 38),
        Boots("Boots3", "male", "advanced", 44),
    ]

    fasteners = [
        Fasteners("Fasteners1", "male", "intermediate", "M"),
        Fasteners("Fasteners2", "female", "beginner", "S"),
        Fasteners("Fasteners3", "male", "advanced", "L"),
    ]

    helmets = [
        Helmet("Helmet1", "male", "L"),
        Helmet("Helmet2", "female", "M"),
        Helmet("Helmet3", "male", "XL"),
    ]

    # Запуск интерактивного меню
    interactive_menu(user, boards, boots, fasteners, helmets)


if __name__ == "__main__":
    main()