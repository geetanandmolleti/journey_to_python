from abc import ABC, abstractmethod


# 1. THE ABSTRACTION (The simple control)
class Switch(ABC):
    @abstractmethod
    def flip(self):
        pass


# 2. THE COMPLEXITY (The hidden wiring)
class WallSwitch(Switch):
    def flip(self):
        # Messy inner details happen automatically
        return "⚡ Electricity flows... Filament heats up... LIGHT ON!"


# --- How you use it ---
my_switch = WallSwitch()

# You just flip the switch. You don't worry about the physics.
print(my_switch.flip())
