import random


class DogNameHelper:

    @staticmethod
    def get_dog_name() -> str:
        available_dog_names = ("Max",
                               "Buddy",
                               "Charlie",
                               "Jack",
                               "Cooper",
                               "Rocky",
                               "Toby",
                               "Tucker",
                               "Jake",
                               "Bear",
                               "Duke",
                               "Teddy",
                               "Oliver",
                               "Riley",
                               "Bailey",
                               "Bentley",
                               "Milo",
                               "Buster",
                               "Cody",
                               "Dexter",
                               "Winston",
                               "Murphy",
                               "Leo",
                               "Lucky",
                               "Oscar",
                               "Louie",
                               "Zeus",
                               "Henry",
                               "Sam",
                               "Harley",
                               "Baxter",
                               "Gus",
                               "Sammy",
                               "Jackson",
                               "Bruno",
                               "Diesel",
                               "Jax",
                               "Gizmo",
                               "Bandit",
                               "Rusty",
                               "Marley",
                               "Jasper",
                               "Brody",
                               "Roscoe",
                               "Hank",
                               "Otis",
                               "Bo",
                               "Joey",
                               "Beau",
                               "Ollie",
                               "Tank",
                               "Shadow",
                               "Peanut",
                               "Hunter",
                               "Scout",
                               "Blue",
                               "Rocco",
                               "Simba",
                               "Tyson",
                               "Ziggy",
                               "Boomer",
                               "Romeo",
                               "Apollo",
                               "Ace",
                               "Luke",
                               "Rex",
                               "Finn",
                               "Chance",
                               "Rudy",
                               "Loki",
                               "Moose",
                               "George",
                               "Samson",
                               "Coco",
                               "Benny",
                               "Thor",
                               "Rufus",
                               "Prince",
                               "Chester",
                               "Brutus",
                               "Scooter",
                               "Chico",
                               "Spike",
                               "Gunner",
                               "Sparky",
                               "Mickey",
                               "Kobe",
                               "Chase",
                               "Oreo",
                               "Frankie",
                               "Mac",
                               "Benji",
                               "Bubba",
                               "Champ",
                               "Brady",
                               "Elvis",
                               "Copper",
                               "Cash",
                               "Archie",
                               "Walter")

        random_index = random.randint(0, len(available_dog_names) - 1)

        return available_dog_names[random_index]
