#!/usr/bin/env python3
"""
🎮 Mystery Island Adventure Game 🏝️
A fun text-based adventure game where you explore a mysterious island!
"""

import random
import time
import sys

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def slow_print(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    """Print game banner"""
    banner = f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════╗
║  🏝️  MYSTERY ISLAND ADVENTURE  🏝️                   ║
║                                                       ║
║  You wake up on a strange island...                  ║
║  Can you find the treasure and escape?               ║
╚═══════════════════════════════════════════════════════╝{Colors.END}
"""
    print(banner)

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.score = 0
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"{Colors.GREEN}✓ Added {item} to inventory!{Colors.END}")
    
    def show_inventory(self):
        if self.inventory:
            print(f"\n{Colors.CYAN}🎒 Your inventory:{Colors.END}")
            for item in self.inventory:
                print(f"  • {item}")
        else:
            print(f"{Colors.YELLOW}Your inventory is empty.{Colors.END}")
    
    def show_stats(self):
        print(f"\n{Colors.BOLD}━━━ Player Stats ━━━{Colors.END}")
        print(f"Name: {self.name}")
        print(f"Health: {Colors.GREEN}{'❤️ ' * (self.health // 20)}{Colors.END} ({self.health}/100)")
        print(f"Score: {self.score}")

class Game:
    def __init__(self):
        self.player = None
        self.current_location = "beach"
        self.game_over = False
        
    def start(self):
        """Start the game"""
        print_banner()
        slow_print(f"\n{Colors.YELLOW}Welcome, adventurer!{Colors.END}")
        name = input(f"\n{Colors.CYAN}What is your name? {Colors.END}").strip()
        
        if not name:
            name = "Explorer"
        
        self.player = Player(name)
        slow_print(f"\nWelcome, {Colors.BOLD}{self.player.name}{Colors.END}!")
        time.sleep(1)
        
        slow_print(f"\n{Colors.YELLOW}You wake up on a mysterious island...{Colors.END}")
        slow_print("The sun is shining, waves are crashing, and adventure awaits!")
        time.sleep(1)
        
        self.game_loop()
    
    def game_loop(self):
        """Main game loop"""
        while not self.game_over and self.player.health > 0:
            self.show_location()
            self.show_options()
            choice = self.get_choice()
            self.process_choice(choice)
        
        self.end_game()
    
    def show_location(self):
        """Show current location description"""
        locations = {
            "beach": {
                "desc": f"\n{Colors.CYAN}🏖️  THE BEACH{Colors.END}\nYou're standing on a beautiful sandy beach. To the north, you see a dense jungle. To the east, there's a mysterious cave.",
                "emoji": "🏖️"
            },
            "jungle": {
                "desc": f"\n{Colors.GREEN}🌴  THE JUNGLE{Colors.END}\nYou're surrounded by thick vegetation and exotic sounds. You spot something glittering in the trees!",
                "emoji": "🌴"
            },
            "cave": {
                "desc": f"\n{Colors.BLUE}🕳️  THE CAVE{Colors.END}\nA dark, mysterious cave. You hear water dripping and see ancient symbols on the walls.",
                "emoji": "🕳️"
            },
            "temple": {
                "desc": f"\n{Colors.YELLOW}🏛️  ANCIENT TEMPLE{Colors.END}\nAn ancient temple stands before you, covered in vines. This must be where the treasure is hidden!",
                "emoji": "🏛️"
            }
        }
        
        print("\n" + "="*60)
        print(locations[self.current_location]["desc"])
        print("="*60)
    
    def show_options(self):
        """Show available actions"""
        options = {
            "beach": [
                "1. Explore the jungle to the north",
                "2. Enter the mysterious cave to the east",
                "3. Search the beach",
                "4. Check inventory",
                "5. View stats"
            ],
            "jungle": [
                "1. Investigate the glittering object",
                "2. Continue deeper into the jungle",
                "3. Return to the beach",
                "4. Check inventory",
                "5. View stats"
            ],
            "cave": [
                "1. Light a torch and explore deeper",
                "2. Examine the ancient symbols",
                "3. Return to the beach",
                "4. Check inventory",
                "5. View stats"
            ],
            "temple": [
                "1. Enter the temple",
                "2. Search around the temple",
                "3. Return to jungle",
                "4. Check inventory",
                "5. View stats"
            ]
        }
        
        print(f"\n{Colors.BOLD}What do you want to do?{Colors.END}")
        for option in options[self.current_location]:
            print(f"  {option}")
    
    def get_choice(self):
        """Get player choice"""
        while True:
            try:
                choice = input(f"\n{Colors.CYAN}Enter your choice (1-5): {Colors.END}").strip()
                if choice in ['1', '2', '3', '4', '5']:
                    return choice
                else:
                    print(f"{Colors.RED}Invalid choice. Please enter 1-5.{Colors.END}")
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Thanks for playing!{Colors.END}")
                sys.exit(0)
    
    def process_choice(self, choice):
        """Process player's choice based on location"""
        if choice == '4':
            self.player.show_inventory()
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
            return
        
        if choice == '5':
            self.player.show_stats()
            input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
            return
        
        # Location-specific choices
        if self.current_location == "beach":
            if choice == '1':
                slow_print(f"\n{Colors.GREEN}You venture into the jungle...{Colors.END}")
                time.sleep(1)
                self.current_location = "jungle"
            elif choice == '2':
                slow_print(f"\n{Colors.BLUE}You cautiously enter the dark cave...{Colors.END}")
                time.sleep(1)
                self.current_location = "cave"
            elif choice == '3':
                self.beach_search()
        
        elif self.current_location == "jungle":
            if choice == '1':
                self.find_compass()
            elif choice == '2':
                self.discover_temple()
            elif choice == '3':
                slow_print(f"\n{Colors.CYAN}You head back to the beach...{Colors.END}")
                time.sleep(1)
                self.current_location = "beach"
        
        elif self.current_location == "cave":
            if choice == '1':
                self.explore_cave()
            elif choice == '2':
                self.decipher_symbols()
            elif choice == '3':
                slow_print(f"\n{Colors.CYAN}You exit the cave back to the beach...{Colors.END}")
                time.sleep(1)
                self.current_location = "beach"
        
        elif self.current_location == "temple":
            if choice == '1':
                self.enter_temple()
            elif choice == '2':
                self.search_temple_area()
            elif choice == '3':
                slow_print(f"\n{Colors.GREEN}You return to the jungle...{Colors.END}")
                time.sleep(1)
                self.current_location = "jungle"
    
    def beach_search(self):
        """Search the beach"""
        items = ["seashell", "driftwood", "mysterious bottle"]
        if "seashell" not in self.player.inventory:
            found_item = random.choice(items)
            slow_print(f"\n{Colors.YELLOW}You search the beach...{Colors.END}")
            time.sleep(1)
            slow_print(f"You found a {found_item}!")
            self.player.add_item(found_item)
            self.player.score += 10
        else:
            slow_print(f"\n{Colors.YELLOW}You've already searched this area thoroughly.{Colors.END}")
    
    def find_compass(self):
        """Find the compass in the jungle"""
        if "compass" not in self.player.inventory:
            slow_print(f"\n{Colors.GREEN}You push through the foliage...{Colors.END}")
            time.sleep(1)
            slow_print("It's an old compass! This could help you navigate the island.")
            self.player.add_item("compass")
            self.player.score += 25
        else:
            slow_print(f"\n{Colors.YELLOW}You've already taken the compass.{Colors.END}")
    
    def discover_temple(self):
        """Discover the ancient temple"""
        if "compass" in self.player.inventory:
            slow_print(f"\n{Colors.GREEN}Using the compass, you navigate deeper into the jungle...{Colors.END}")
            time.sleep(1)
            slow_print(f"{Colors.YELLOW}You discover an ancient temple!{Colors.END}")
            self.current_location = "temple"
            self.player.score += 30
        else:
            slow_print(f"\n{Colors.RED}You get lost in the dense jungle and return to where you started.{Colors.END}")
            slow_print(f"{Colors.YELLOW}Maybe you need something to help you navigate...{Colors.END}")
    
    def explore_cave(self):
        """Explore deeper into the cave"""
        if "torch" in self.player.inventory:
            slow_print(f"\n{Colors.BLUE}You light your torch and venture deeper...{Colors.END}")
            time.sleep(1)
            slow_print("You find a hidden chamber with ancient artifacts!")
            if "ancient key" not in self.player.inventory:
                self.player.add_item("ancient key")
                self.player.score += 40
        else:
            slow_print(f"\n{Colors.RED}It's too dark to explore safely. You need a light source!{Colors.END}")
    
    def decipher_symbols(self):
        """Examine the cave symbols"""
        slow_print(f"\n{Colors.BLUE}You study the ancient symbols on the wall...{Colors.END}")
        time.sleep(1)
        slow_print("The symbols seem to tell a story about a great treasure...")
        slow_print(f"{Colors.YELLOW}You notice a torch mounted on the wall!{Colors.END}")
        if "torch" not in self.player.inventory:
            self.player.add_item("torch")
            self.player.score += 15
    
    def search_temple_area(self):
        """Search around the temple"""
        slow_print(f"\n{Colors.YELLOW}You search around the temple grounds...{Colors.END}")
        time.sleep(1)
        if random.random() > 0.5:
            slow_print("You find some ancient coins!")
            self.player.score += 20
        else:
            slow_print("You find nothing of interest.")
    
    def enter_temple(self):
        """Enter the temple and potentially win the game"""
        if "ancient key" in self.player.inventory:
            slow_print(f"\n{Colors.YELLOW}You use the ancient key to unlock the temple doors...{Colors.END}")
            time.sleep(1)
            slow_print(f"{Colors.GREEN}The doors creak open, revealing a chamber filled with golden treasure!{Colors.END}")
            time.sleep(1)
            slow_print(f"\n{Colors.BOLD}{Colors.YELLOW}🎉 CONGRATULATIONS! 🎉{Colors.END}")
            slow_print("You've found the legendary treasure of Mystery Island!")
            self.player.score += 100
            self.game_over = True
        else:
            slow_print(f"\n{Colors.YELLOW}The temple doors are locked with an ancient mechanism...{Colors.END}")
            slow_print(f"{Colors.RED}You need to find a key to enter.{Colors.END}")
    
    def end_game(self):
        """End the game and show final score"""
        print(f"\n\n{Colors.CYAN}{'='*60}{Colors.END}")
        if self.player.health <= 0:
            print(f"{Colors.RED}💀 GAME OVER 💀{Colors.END}")
            print("You have perished on Mystery Island...")
        else:
            print(f"{Colors.GREEN}🎮 GAME COMPLETE 🎮{Colors.END}")
        
        print(f"\n{Colors.BOLD}Final Score: {self.player.score} points{Colors.END}")
        
        if self.player.score >= 200:
            print(f"{Colors.YELLOW}⭐⭐⭐ LEGENDARY EXPLORER! ⭐⭐⭐{Colors.END}")
        elif self.player.score >= 100:
            print(f"{Colors.GREEN}⭐⭐ SKILLED ADVENTURER! ⭐⭐{Colors.END}")
        elif self.player.score >= 50:
            print(f"{Colors.CYAN}⭐ CURIOUS EXPLORER! ⭐{Colors.END}")
        else:
            print(f"{Colors.BLUE}Keep exploring to find more secrets!{Colors.END}")
        
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"\n{Colors.YELLOW}Thanks for playing, {self.player.name}!{Colors.END}\n")

def main():
    """Main entry point"""
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

