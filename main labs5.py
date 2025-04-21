import logging
from datetime import datetime
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.INFO,
    filename='equipment_log.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def log_action(message):
    """Функция для логирования действий"""
    logging.info(message)
    print(f"LOG: {message}")

class CustomError(BaseException):
    pass

class InvalidInputError(CustomError):
    pass

class EquipmentNotFoundError(CustomError):
    pass

class Equipment(ABC):
    total_equipment = 0

    def __init__(self, name, gender, skill):
        Equipment.total_equipment += 1
        self.name = name
        self.gender = gender
        self.skill = skill
        self.created_at = datetime.now()
        log_action(f"Created Equipment: {name} ({self.__class__.__name__})")

    @staticmethod
    def get_total_equipment():
        return Equipment.total_equipment

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
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

    @abstractmethod
    def get_usage_instructions(self):
        """Полиморфный метод для получения инструкций по использованию"""
        pass

    @abstractmethod
    def calculate_rental_price(self, days):
        """Полиморфный метод для расчета цены аренды"""
        pass

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
        log_action(f"Created User: {name}")

    def __str__(self):
        return (f"User(Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Skill: {self.skill}, "
                f"Height: {self.height}, Weight: {self.weight}, Clothing Size: {self.clothing_size}, "
                f"Leg Size: {self.leg_size}, Fasteners Size: {self.fasteners}, Helmet Size: {self.helmet_size})")

    def __repr__(self):
        return (f"User(name='{self.name}', age={self.age}, gender='{self.gender}', skill='{self.skill}', "
                f"height={self.height}, weight={self.weight}, clothing_size='{self.clothing_size}', "
                f"leg_size={self.leg_size}, fasteners_size='{self.fasteners}', helmet_size='{self.helmet_size}')")

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
            raise InvalidInputError(f"Invalid input: {e}")

    def update_skill(self, new_skill):
        self.skill = new_skill
        log_action(f"User {self.name} skill updated to: {self.skill}")
        print(f"Skill updated to: {self.skill}")

class Board(Equipment):
    def __init__(self, name, gender, skill, height):
        super().__init__(name, gender, skill)
        self.height = height
        self.type = "Snowboard"

    def __str__(self):
        return f"Board(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill}, Height: {self.height})"

    def __repr__(self):
        return f"Board(name='{self.name}', gender='{self.gender}', skill='{self.skill}', height={self.height})"

    def get_usage_instructions(self):
        return f"Attach boots to {self.name} board using fasteners. Suitable for {self.skill} level."

    def calculate_rental_price(self, days):
        base_price = 30 if self.skill == "beginner" else 40 if self.skill == "intermediate" else 50
        return base_price * days * (1 + 0.1 * (self.height / 100))

    def perform_trick(self, trick_name):
        log_action(f"Board {self.name} performing trick: {trick_name}")
        return f"{self.name} is performing {trick_name} trick!"

    @classmethod
    def from_input(cls):
        try:
            name = input("Enter board name: ")
            gender = input("Enter gender: ")
            skill = input("Enter skill level (beginner, intermediate, advanced): ")
            height = float(input("Enter recommended height (in cm): "))
            return cls(name, gender, skill, height)
        except ValueError as e:
            raise InvalidInputError(f"Invalid input: {e}")

class Boots(Equipment):
    def __init__(self, name, gender, skill, leg_size):
        super().__init__(name, gender, skill)
        self.leg_size = leg_size
        self.comfort_level = "medium"

    def __str__(self):
        return f"Boots(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill}, Leg Size: {self.leg_size})"

    def __repr__(self):
        return f"Boots(name='{self.name}', gender='{self.gender}', skill='{self.skill}', leg_size={self.leg_size})"

    def get_usage_instructions(self):
        return f"Wear {self.name} boots and secure them properly. Size: {self.leg_size}"

    def calculate_rental_price(self, days):
        return 15 * days * (1.2 if self.gender == "female" else 1.0)

    def adjust_comfort(self, level):
        self.comfort_level = level
        log_action(f"Boots {self.name} comfort adjusted to {level}")
        return f"Comfort level adjusted to {level}"

    @classmethod
    def from_input(cls):
        try:
            name = input("Enter boots name: ")
            gender = input("Enter gender: ")
            skill = input("Enter skill level (beginner, intermediate, advanced): ")
            leg_size = float(input("Enter leg size (in cm): "))
            return cls(name, gender, skill, leg_size)
        except ValueError as e:
            raise InvalidInputError(f"Invalid input: {e}")

class Fasteners(Equipment):
    def __init__(self, name, gender, skill, fasteners_size):
        super().__init__(name, gender, skill)
        self.fasteners = fasteners_size
        self.adjustment = "medium"

    def __str__(self):
        return f"Fasteners(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill}, Fasteners Size: {self.fasteners})"

    def __repr__(self):
        return f"Fasteners(name='{self.name}', gender='{self.gender}', skill='{self.skill}', fasteners_size='{self.fasteners}')"

    def get_usage_instructions(self):
        return f"Use {self.name} fasteners to secure boots to board. Size: {self.fasteners}"

    def calculate_rental_price(self, days):
        return 10 * days

    def adjust_tightness(self, level):
        self.adjustment = level
        log_action(f"Fasteners {self.name} tightness adjusted to {level}")
        return f"Tightness adjusted to {level}"

    @classmethod
    def from_input(cls):
        try:
            name = input("Enter fasteners name: ")
            gender = input("Enter gender: ")
            skill = input("Enter skill level (beginner, intermediate, advanced): ")
            fasteners_size = input("Enter fasteners size: ")
            return cls(name, gender, skill, fasteners_size)
        except ValueError as e:
            raise InvalidInputError(f"Invalid input: {e}")

class Helmet(Equipment):
    def __init__(self, name, gender, helmet_size):
        super().__init__(name, gender, "all")
        self.size = helmet_size
        self.ventilation = "open"

    def __str__(self):
        return f"Helmet(Name: {self.name}, Gender: {self.gender}, Size: {self.size})"

    def __repr__(self):
        return f"Helmet(name='{self.name}', gender='{self.gender}', helmet_size='{self.size}')"

    def get_usage_instructions(self):
        return f"Wear {self.name} helmet and secure the strap. Size: {self.size}"

    def calculate_rental_price(self, days):
        return 8 * days * (1.1 if self.gender == "female" else 1.0)

    def adjust_ventilation(self, status):
        self.ventilation = status
        log_action(f"Helmet {self.name} ventilation adjusted to {status}")
        return f"Ventilation adjusted to {status}"

    @classmethod
    def from_input(cls):
        try:
            name = input("Enter helmet name: ")
            gender = input("Enter gender: ")
            helmet_size = input("Enter helmet size: ")
            return cls(name, gender, helmet_size)
        except ValueError as e:
            raise InvalidInputError(f"Invalid input: {e}")

class EquipmentManager:
    @staticmethod
    def find_max_value(items_2d, attribute="height"):
        if not items_2d or not any(items_2d):
            raise ValueError("The list is empty or contains no elements.")

        max_item = None
        max_value = float('-inf')

        for row in items_2d:
            for item in row:
                if not hasattr(item, attribute):
                    raise AttributeError(f"Attribute '{attribute}' does not exist in the object.")
                current_value = getattr(item, attribute)
                if current_value > max_value:
                    max_value = current_value
                    max_item = item

        return max_item

class BaseEquipment(Equipment):
    def __init__(self, name, gender, skill):
        super().__init__(name, gender, skill)

    def display_info(self):
        print(f"Base Equipment Info: {self.name}, {self.gender}, {self.skill}")

    def __str__(self):
        return f"BaseEquipment(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill})"

    def __repr__(self):
        return f"BaseEquipment(name='{self.name}', gender='{self.gender}', skill='{self.skill}')"

    def get_usage_instructions(self):
        return "Basic usage instructions for all equipment"

    def calculate_rental_price(self, days):
        return 20 * days

class DerivedEquipment(BaseEquipment):
    def __init__(self, name, gender, skill, additional_info):
        super().__init__(name, gender, skill)
        self.additional_info = additional_info

    def display_info(self):
        print(f"Derived Equipment Info: {self.name}, {self.gender}, {self.skill}, {self.additional_info}")

    def call_base_display(self):
        super().display_info()

    def conditional_display(self, condition):
        if condition:
            self.display_info()
        else:
            super().display_info()

    def __str__(self):
        return f"DerivedEquipment(Name: {self.name}, Gender: {self.gender}, Skill: {self.skill}, Additional Info: {self.additional_info})"

    def __repr__(self):
        return f"DerivedEquipment(name='{self.name}', gender='{self.gender}', skill='{self.skill}', additional_info='{self.additional_info}')"

    def get_usage_instructions(self):
        return f"Special instructions: {self.additional_info}"

    def calculate_rental_price(self, days):
        return super().calculate_rental_price(days) * 1.5

def recommend_board(user, boards):
    for board in boards:
        if (board.gender == user.gender and
            board.skill == user.skill and
            board.height >= user.height - 10 and
            board.height <= user.height + 10):
            log_action(f"Recommended board: {board.name} for user {user.name}")
            return board
    raise EquipmentNotFoundError("No suitable board found.")

def recommend_boots(user, boots):
    for boot in boots:
        if (boot.gender == user.gender and
            boot.skill == user.skill and
            boot.leg_size == user.leg_size):
            log_action(f"Recommended boots: {boot.name} for user {user.name}")
            return boot
    raise EquipmentNotFoundError("No suitable boots found.")

def recommend_fasteners(user, fasteners):
    for fastener in fasteners:
        if (fastener.gender == user.gender and
            fastener.skill == user.skill and
            fastener.fasteners == user.fasteners):
            log_action(f"Recommended fasteners: {fastener.name} for user {user.name}")
            return fastener
    raise EquipmentNotFoundError("No suitable fasteners found.")

def recommend_helmet(user, helmets):
    for helmet in helmets:
        if (helmet.gender == user.gender and
            helmet.size == user.helmet_size):
            log_action(f"Recommended helmet: {helmet.name} for user {user.name}")
            return helmet
    raise EquipmentNotFoundError("No suitable helmet found.")

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

        try:
            if choice == "1":
                user.name = input("Enter new name: ")
                log_action(f"User name updated to: {user.name}")
            elif choice == "2":
                user.age = int(input("Enter new age: "))
                log_action(f"User age updated to: {user.age}")
            elif choice == "3":
                user.gender = input("Enter new gender: ")
                log_action(f"User gender updated to: {user.gender}")
            elif choice == "4":
                user.skill = input("Enter new skill level (beginner, intermediate, advanced): ")
                log_action(f"User skill updated to: {user.skill}")
            elif choice == "5":
                user.height = float(input("Enter new height (in cm): "))
                log_action(f"User height updated to: {user.height}")
            elif choice == "6":
                user.weight = float(input("Enter new weight (in kg): "))
                log_action(f"User weight updated to: {user.weight}")
            elif choice == "7":
                user.clothing_size = input("Enter new clothing size: ")
                log_action(f"User clothing size updated to: {user.clothing_size}")
            elif choice == "8":
                user.leg_size = float(input("Enter new leg size (in cm): "))
                log_action(f"User leg size updated to: {user.leg_size}")
            elif choice == "9":
                user.fasteners = input("Enter new fasteners size: ")
                log_action(f"User fasteners size updated to: {user.fasteners}")
            elif choice == "10":
                user.helmet_size = input("Enter new helmet size: ")
                log_action(f"User helmet size updated to: {user.helmet_size}")
            elif choice == "11":
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    return user

def interactive_menu(user, boards, boots, fasteners, helmets):
    equipment_manager = EquipmentManager()
    equipment_1d = []
    equipment_2d = []
    base_equipment = None
    derived_equipment = None
    
    filter_by_gender = lambda items, gender: list(filter(lambda x: x.gender == gender, items))
    sort_by_name = lambda items: sorted(items, key=lambda x: x.name)
    calculate_total_rental = lambda items, days: sum(item.calculate_rental_price(days) for item in items)
    print_instructions = lambda items: [print(f"{item.name}: {item.get_usage_instructions()}") for item in items]

    while True:
        print("\n1. Add a new board")
        print("2. Add new boots")
        print("3. Add new fasteners")
        print("4. Add a new helmet")
        print("5. Recommend equipment")
        print("6. Edit user information")
        print("7. Create 1D list of equipment")
        print("8. Create 2D list of equipment")
        print("9. Find object with max attribute value in 2D list")
        print("10. Create BaseEquipment object")
        print("11. Create DerivedEquipment object")
        print("12. Call display_info method of BaseEquipment")
        print("13. Call display_info method of DerivedEquipment")
        print("14. Call call_base_display method of DerivedEquipment")
        print("15. Call conditional_display method of DerivedEquipment")
        print("16. Filter equipment by gender (lambda)")
        print("17. Sort equipment by name (lambda)")
        print("18. Calculate total rental price (lambda)")
        print("19. Print usage instructions (lambda)")
        print("20. Exit")
        choice = input("Enter your choice: ")

        try:
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
                try:
                    recommended_board = recommend_board(user, boards)
                    print("\nRecommended Board:")
                    print(recommended_board.format_info())
                    print("Usage:", recommended_board.get_usage_instructions())
                    print(f"Rental price for 3 days: ${recommended_board.calculate_rental_price(3):.2f}")
                except EquipmentNotFoundError as e:
                    print(f"\n{e}")

                try:
                    recommended_boots = recommend_boots(user, boots)
                    print("\nRecommended Boots:")
                    print(recommended_boots.format_info())
                    print("Usage:", recommended_boots.get_usage_instructions())
                    print(f"Rental price for 3 days: ${recommended_boots.calculate_rental_price(3):.2f}")
                except EquipmentNotFoundError as e:
                    print(f"\n{e}")

                try:
                    recommended_fasteners = recommend_fasteners(user, fasteners)
                    print("\nRecommended Fasteners:")
                    print(recommended_fasteners.format_info())
                    print("Usage:", recommended_fasteners.get_usage_instructions())
                    print(f"Rental price for 3 days: ${recommended_fasteners.calculate_rental_price(3):.2f}")
                except EquipmentNotFoundError as e:
                    print(f"\n{e}")

                try:
                    recommended_helmet = recommend_helmet(user, helmets)
                    print("\nRecommended Helmet:")
                    print(recommended_helmet.format_info())
                    print("Usage:", recommended_helmet.get_usage_instructions())
                    print(f"Rental price for 3 days: ${recommended_helmet.calculate_rental_price(3):.2f}")
                except EquipmentNotFoundError as e:
                    print(f"\n{e}")
            elif choice == "6":
                print("\nEditing user information:")
                user = edit_user_info(user)
            elif choice == "7":
                print("\nCreating 1D list of equipment:")
                equipment_1d = []
                while True:
                    print("\n1. Add Board")
                    print("2. Add Boots")
                    print("3. Add Fasteners")
                    print("4. Add Helmet")
                    print("5. Finish creating 1D list")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        new_board = Board.from_input()
                        equipment_1d.append(new_board)
                    elif sub_choice == "2":
                        new_boots = Boots.from_input()
                        equipment_1d.append(new_boots)
                    elif sub_choice == "3":
                        new_fasteners = Fasteners.from_input()
                        equipment_1d.append(new_fasteners)
                    elif sub_choice == "4":
                        new_helmet = Helmet.from_input()
                        equipment_1d.append(new_helmet)
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid choice. Please try again.")
                print("\n1D list created:")
                for item in equipment_1d:
                    print(item)
            elif choice == "8":
                print("\nCreating 2D list of equipment:")
                equipment_2d = []
                while True:
                    print("\n1. Add a new row")
                    print("2. Finish creating 2D list")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        row = []
                        while True:
                            print("\n1. Add Board")
                            print("2. Add Boots")
                            print("3. Add Fasteners")
                            print("4. Add Helmet")
                            print("5. Finish current row")
                            item_choice = input("Enter your choice: ")

                            if item_choice == "1":
                                new_board = Board.from_input()
                                row.append(new_board)
                            elif item_choice == "2":
                                new_boots = Boots.from_input()
                                row.append(new_boots)
                            elif item_choice == "3":
                                new_fasteners = Fasteners.from_input()
                                row.append(new_fasteners)
                            elif item_choice == "4":
                                new_helmet = Helmet.from_input()
                                row.append(new_helmet)
                            elif item_choice == "5":
                                break
                            else:
                                print("Invalid choice. Please try again.")
                        equipment_2d.append(row)
                    elif sub_choice == "2":
                        break
                    else:
                        print("Invalid choice. Please try again.")
                print("\n2D list created:")
                for row in equipment_2d:
                    for item in row:
                        print(item)
            elif choice == "9":
                if not equipment_2d:
                    print("\n2D list is empty. Please create a 2D list first.")
                else:
                    attribute = input("\nEnter attribute to find max value (e.g., height, leg_size): ")
                    try:
                        max_item = equipment_manager.find_max_value(equipment_2d, attribute)
                        print(f"\nObject with max {attribute} in 2D list: {max_item}")
                    except ValueError as e:
                        print(f"\nError: {e}")
                    except AttributeError as e:
                        print(f"\nError: {e}")
            elif choice == "10":
                name = input("Enter name for BaseEquipment: ")
                gender = input("Enter gender: ")
                skill = input("Enter skill level (beginner, intermediate, advanced): ")
                base_equipment = BaseEquipment(name, gender, skill)
                print("BaseEquipment object created.")
            elif choice == "11":
                name = input("Enter name for DerivedEquipment: ")
                gender = input("Enter gender: ")
                skill = input("Enter skill level (beginner, intermediate, advanced): ")
                additional_info = input("Enter additional info: ")
                derived_equipment = DerivedEquipment(name, gender, skill, additional_info)
                print("DerivedEquipment object created.")
            elif choice == "12":
                if base_equipment:
                    base_equipment.display_info()
                else:
                    print("BaseEquipment object not created yet.")
            elif choice == "13":
                if derived_equipment:
                    derived_equipment.display_info()
                else:
                    print("DerivedEquipment object not created yet.")
            elif choice == "14":
                if derived_equipment:
                    derived_equipment.call_base_display()
                else:
                    print("DerivedEquipment object not created yet.")
            elif choice == "15":
                if derived_equipment:
                    condition = input("Enter condition (True/False): ").lower() == 'true'
                    derived_equipment.conditional_display(condition)
                else:
                    print("DerivedEquipment object not created yet.")
            elif choice == "16":
                gender = input("Enter gender to filter (male/female): ")
                filtered = filter_by_gender(equipment_1d, gender)
                print(f"\nEquipment for {gender}:")
                for item in filtered:
                    print(item)
            elif choice == "17":
                sorted_eq = sort_by_name(equipment_1d)
                print("\nEquipment sorted by name:")
                for item in sorted_eq:
                    print(item)
            elif choice == "18":
                days = int(input("Enter rental days: "))
                total = calculate_total_rental(equipment_1d, days)
                print(f"\nTotal rental price for {days} days: ${total:.2f}")
            elif choice == "19":
                print("\nUsage instructions:")
                print_instructions(equipment_1d)
            elif choice == "20":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except CustomError as e:
            print(f"An error occurred: {e}")
        finally:
            print("\nReturning to main menu...")

def main():
    try:
        log_action("Program started")
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

        interactive_menu(user, boards, boots, fasteners, helmets)
    except CustomError as e:
        print(f"An error occurred: {e}")
    finally:
        log_action("Program execution completed")
        print("\nProgram execution completed. Check equipment_log.log for details.")

if __name__ == "__main__":
    main()