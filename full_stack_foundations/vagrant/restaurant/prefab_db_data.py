"""
This module provides pre-fab data for restaurants and menu items
that can be added to the database for testing.
"""

from models import Restaurant, MenuItem
from database_utils import get_or_create

PREFAB_RESTAURANTS = {
    "urban_burger": "Urban Burger",
    "super_stir_fry": "Super Stir Fry",
    "panda_garden": "Panda Garden",
    "thyme_for_that": "Thyme for That Vegetarian Cuisine",
    "tonys_bistro": "Tony\'s Bistro ",
    "andalas": "Andala\'s",
    "auntie_anns": "Auntie Ann\'s Diner",
    "cocina_y_amor": "Cocina Y Amor",
    "state_bird": "State Bird Provisions"
}

def create_restaurants(session):
    """Function to create Restaurant objects."""

    for key, val in PREFAB_RESTAURANTS.iteritems():
        PREFAB_RESTAURANTS[key] = get_or_create(
            session, Restaurant, name=val
        )

def create_all_the_things(session):
    """Function to create lots of Restaurant and MenuItem objects."""

    create_restaurants(session)

    # Urban Burger
    ub_mi_1 = get_or_create(session, MenuItem,
                            name="Veggie Burger",
                            description="Juicy grilled veggie patty with "\
                            "tomato mayo and lettuce",
                            price="$7.50", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])

    ub_mi_2 = get_or_create(session, MenuItem,
                            name="French Fries",
                            description="with garlic and parmesan",
                            price="$2.99", course="Appetizer",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])

    ub_mi_3 = get_or_create(session, MenuItem,
                            name="Chicken Burger",
                            description="Juicy grilled chicken patty with "\
                            "tomato mayo and lettuce",
                            price="$5.50", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])

    ub_mi_4 = get_or_create(session, MenuItem,
                            name="Chocolate Cake",
                            description="fresh baked and served with "\
                            "ice cream",
                            price="$3.99", course="Dessert",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])

    ub_mi_5 = get_or_create(session, MenuItem,
                            name="Sirloin Burger",
                            description="Made with grade A beef",
                            price="$7.99", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])

    ub_mi_6 = get_or_create(session, MenuItem,
                            name="Root Beer",
                            description="16oz of refreshing goodness",
                            price="$1.99", course="Beverage",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])

    ub_mi_7 = get_or_create(session, MenuItem,
                            name="Iced Tea",
                            description="with Lemon",
                            price="$.99", course="Beverage",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])

    ub_mi_8 = get_or_create(session, MenuItem,
                            name="Grilled Cheese Sandwich",
                            description="On texas toast with American Cheese",
                            price="$3.49", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["urban_burger"])


    # Super Stir Fry
    ssf_mi_1 = get_or_create(session, MenuItem,
                             name="Chicken Stir Fry",
                             description="With your choice of noodles "\
                             "vegetables and sauces",
                             price="$7.99", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["super_stir_fry"])

    ssf_mi_2 = get_or_create(session, MenuItem,
                             name="Peking Duck",
                             description="A famous duck dish from Beijing "\
                             "that has been prepared since the imperial era. "\
                             "The meat is prized for its thin, crisp skin, "\
                             "with authentic versions of the dish serving "\
                             "mostly the skin and little meat, sliced in "\
                             "front of the diners by the cook",
                             price="$25", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["super_stir_fry"])

    ssf_mi_3 = get_or_create(session, MenuItem,
                             name="Spicy Tuna Roll",
                             description="Seared rare ahi, avocado, edamame, "\
                             "cucumber with wasabi soy sauce ",
                             price="15", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["super_stir_fry"])

    ssf_mi_4 = get_or_create(session, MenuItem,
                             name="Nepali Momo ",
                             description="Steamed dumplings made with "\
                             "vegetables, spices and meat. ",
                             price="12", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["super_stir_fry"])

    ssf_mi_5 = get_or_create(session, MenuItem,
                             name="Beef Noodle Soup",
                             description="A Chinese noodle soup made of "\
                             "stewed or red braised beef, beef broth, "\
                             "vegetables and Chinese noodles.",
                             price="14", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["super_stir_fry"])

    ssf_mi_6 = get_or_create(session, MenuItem,
                             name="Ramen",
                             description="A Japanese noodle soup dish. "\
                             "It consists of Chinese-style wheat noodles "\
                             "served in a meat- or (occasionally) fish-based "\
                             "broth, often flavored with soy sauce or miso, "\
                             "and uses toppings such as sliced pork, dried "\
                             "seaweed, kamaboko, and green onions.",
                             price="12", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["super_stir_fry"])


    # Panda Garden
    pg_mi_1 = get_or_create(session, MenuItem,
                            name="Pho",
                            description="a Vietnamese noodle soup consisting "\
                            "of broth, linguine-shaped rice noodles called "\
                            "banh pho, a few herbs, and meat.",
                            price="$8.99", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["panda_garden"])

    pg_mi_2 = get_or_create(session, MenuItem,
                            name="Chinese Dumplings",
                            description="a common Chinese dumpling which "\
                            "generally consists of minced meat and finely "\
                            "chopped vegetables wrapped into a piece of "\
                            "dough skin. The skin can be either thin and "\
                            "elastic or thicker.",
                            price="$6.99", course="Appetizer",
                            restaurant=PREFAB_RESTAURANTS["panda_garden"])

    pg_mi_3 = get_or_create(session, MenuItem,
                            name="Gyoza",
                            description="The most prominent differences "\
                            "between Japanese-style gyoza and Chinese-style "\
                            "jiaozi are the rich garlic flavor, which is "\
                            "less noticeable in the Chinese version, the "\
                            "light seasoning of Japanese gyoza with salt and "\
                            "soy sauce, and the fact that gyoza wrappers are "\
                            "much thinner",
                            price="$9.95", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["panda_garden"])

    pg_mi_4 = get_or_create(session, MenuItem,
                            name="Stinky Tofu",
                            description="Taiwanese dish, deep fried "\
                            "fermented tofu served with pickled cabbage.",
                            price="$6.99", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["panda_garden"])

    pg_mi_5 = get_or_create(session, MenuItem,
                            name="Veggie Burger",
                            description="Juicy grilled veggie patty with "\
                            "tomato mayo and lettuce",
                            price="$9.50", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["panda_garden"])


    # Thyme for That
    tft_mi_1 = get_or_create(session, MenuItem,
                             name="Tres Leches Cake",
                             description="Rich, luscious sponge cake soaked "\
                             "in sweet milk and topped with vanilla bean "\
                             "whipped cream and strawberries.",
                             price="$2.99", course="Dessert",
                             restaurant=PREFAB_RESTAURANTS["thyme_for_that"])

    tft_mi_2 = get_or_create(session, MenuItem,
                             name="Mushroom risotto",
                             description="Portabello mushrooms in a "\
                             "creamy risotto",
                             price="$5.99", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["thyme_for_that"])

    tft_mi_3 = get_or_create(session, MenuItem,
                             name="Honey Boba Shaved Snow",
                             description="Milk snow layered with honey "\
                             "boba, jasmine tea jelly, grass jelly, "\
                             "caramel, cream, and freshly made mochi",
                             price="$4.50", course="Dessert",
                             restaurant=PREFAB_RESTAURANTS["thyme_for_that"])

    tft_mi_4 = get_or_create(session, MenuItem,
                             name="Cauliflower Manchurian",
                             description="Golden fried cauliflower florets "\
                             "in a midly spiced soya,garlic sauce cooked "\
                             "with fresh cilantro, celery, chilies,ginger "\
                             "& green onions",
                             price="$6.95", course="Appetizer",
                             restaurant=PREFAB_RESTAURANTS["thyme_for_that"])

    tft_mi_5 = get_or_create(session, MenuItem,
                             name="Aloo Gobi Burrito",
                             description="Vegan goodness. Burrito filled "\
                             "with rice, garbanzo beans, curry sauce, "\
                             "potatoes (aloo), fried cauliflower (gobi) "\
                             "and chutney. Nom Nom",
                             price="$7.95", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["thyme_for_that"])

    tft_mi_6 = get_or_create(session, MenuItem,
                             name="Veggie Burger",
                             description="Juicy grilled veggie patty "\
                             "with tomato mayo and lettuce",
                             price="$6.80", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["thyme_for_that"])


    # Tony's Bistro
    tb_mi_1 = get_or_create(session, MenuItem,
                            name="Shellfish Tower",
                            description="Lobster, shrimp, sea snails, "\
                            "crawfish, stacked into a delicious tower",
                            price="$13.95", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["tonys_bistro"])

    tb_mi_2 = get_or_create(session, MenuItem,
                            name="Chicken and Rice",
                            description="Chicken... and rice",
                            price="$4.95", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["tonys_bistro"])

    tb_mi_3 = get_or_create(session, MenuItem,
                            name="Mom's Spaghetti",
                            description="Spaghetti with some incredible "\
                            "tomato sauce made by mom",
                            price="$6.95", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["tonys_bistro"])

    tb_mi_4 = get_or_create(session, MenuItem,
                            name="Choc Full O\' Mint (Smitten\'s Fresh "\
                            "Mint Chip ice cream)",
                            description="Milk, cream, salt, ..., Liquid "\
                            "nitrogen magic",
                            price="$3.95", course="Dessert",
                            restaurant=PREFAB_RESTAURANTS["tonys_bistro"])

    tb_mi_5 = get_or_create(session, MenuItem,
                            name="Tonkatsu Ramen",
                            description="Noodles in a delicious pork-based "\
                            "broth with a soft-boiled egg",
                            price="$7.95", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["tonys_bistro"])


    # Andala's
    and_mi_1 = get_or_create(session, MenuItem,
                             name="Lamb Curry",
                             description="Slow cook that thang in a pool "\
                             "of tomatoes, onions and alllll those tasty "\
                             "Indian spices. Mmmm.",
                             price="$9.95", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["andalas"])

    and_mi_2 = get_or_create(session, MenuItem,
                             name="Chicken Marsala",
                             description="Chicken cooked in Marsala wine "\
                             "sauce with mushrooms",
                             price="$7.95", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["andalas"])

    and_mi_3 = get_or_create(session, MenuItem,
                             name="Potstickers",
                             description="Delicious chicken and veggies "\
                             "encapsulated in fried dough.",
                             price="$6.50", course="Appetizer",
                             restaurant=PREFAB_RESTAURANTS["andalas"])

    and_mi_4 = get_or_create(session, MenuItem,
                             name="Nigiri Sampler",
                             description="Maguro, Sake, Hamachi, Unagi, "\
                             "Uni, TORO!",
                             price="$6.75", course="Appetizer",
                             restaurant=PREFAB_RESTAURANTS["andalas"])

    and_mi_5 = get_or_create(session, MenuItem,
                             name="Veggie Burger",
                             description="Juicy grilled veggie patty with "\
                             "tomato mayo and lettuce",
                             price="$7.00", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["andalas"])


    # Auntie Ann's
    aa_mi_1 = get_or_create(session, MenuItem,
                            name="Chicken Fried Steak",
                            description="Fresh battered sirloin steak fried "\
                            "and smothered with cream gravy",
                            price="$8.99", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["auntie_anns"])

    aa_mi_2 = get_or_create(session, MenuItem,
                            name="Boysenberry Sorbet",
                            description="An unsettlingly huge amount of "\
                            "ripe berries turned into frozen (and seedless) "\
                            "awesomeness",
                            price="$2.99", course="Dessert",
                            restaurant=PREFAB_RESTAURANTS["auntie_anns"])

    aa_mi_3 = get_or_create(session, MenuItem,
                            name="Broiled salmon",
                            description="Salmon fillet marinated with "\
                            "fresh herbs and broiled hot & fast",
                            price="$10.95", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["auntie_anns"])

    aa_mi_4 = get_or_create(session, MenuItem,
                            name="Morels on toast (seasonal)",
                            description="Wild morel mushrooms fried in "\
                            "butter, served on herbed toast slices",
                            price="$7.50", course="Appetizer",
                            restaurant=PREFAB_RESTAURANTS["auntie_anns"])

    aa_mi_5 = get_or_create(session, MenuItem,
                            name="Tandoori Chicken",
                            description="Chicken marinated in yoghurt and "\
                            "seasoned with a spicy mix(chilli, tamarind "\
                            "among others) and slow cooked in a cylindrical "\
                            "clay or metal oven which gets its heat from "\
                            "burning charcoal.",
                            price="$8.95", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["auntie_anns"])

    aa_mi_6 = get_or_create(session, MenuItem,
                            name="Veggie Burger",
                            description="Juicy grilled veggie patty with "\
                            "tomato mayo and lettuce",
                            price="$9.50", course="Entree",
                            restaurant=PREFAB_RESTAURANTS["auntie_anns"])

    aa_mi_7 = get_or_create(session, MenuItem,
                            name="Spinach Ice Cream",
                            description="vanilla ice cream made with "\
                            "organic spinach leaves",
                            price="$1.99", course="Dessert",
                            restaurant=PREFAB_RESTAURANTS["auntie_anns"])


    # Cocina Y Amor
    cya_mi_1 = get_or_create(session, MenuItem,
                             name="Super Burrito Al Pastor",
                             description="Marinated Pork, Rice, Beans, "\
                             "Avocado, Cilantro, Salsa, Tortilla",
                             price="$5.95", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["cocina_y_amor"])

    cya_mi_2 = get_or_create(session, MenuItem,
                             name="Cachapa",
                             description="Golden brown, corn-based "\
                             "Venezuelan pancake; usually stuffed with "\
                             "queso telita or queso de mano, and possibly "\
                             "lechon.",
                             price="$7.99", course="Entree",
                             restaurant=PREFAB_RESTAURANTS["cocina_y_amor"])


    # State Bird Provisions
    sb_mi_1 = get_or_create(session, MenuItem,
                            name="Chantrelle Toast",
                            description="Crispy Toast with Sesame Seeds "\
                            "slathered with buttery chantrelle mushrooms",
                            price="$5.95", course="Appetizer",
                            restaurant=PREFAB_RESTAURANTS["state_bird"])

    sb_mi_2 = get_or_create(session, MenuItem,
                            name="Guanciale Chawanmushi",
                            description="Japanese egg custard served hot "\
                            "with spicey Italian Pork Jowl (guanciale)",
                            price="$6.95", course="Dessert",
                            restaurant=PREFAB_RESTAURANTS["state_bird"])

    sb_mi_3 = get_or_create(session, MenuItem,
                            name="Lemon Curd Ice Cream Sandwich",
                            description="Lemon Curd Ice Cream Sandwich "\
                            "on a chocolate macaron with cardamom meringue "\
                            "and cashews",
                            price="$4.25", course="Dessert",
                            restaurant=PREFAB_RESTAURANTS["state_bird"])
