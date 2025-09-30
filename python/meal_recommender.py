vegetarian=input("Are you vegetarian ? (yes/no)")
spicy=input("Do you like spicy food ? (yes/no)")
vegetarian=vegetarian.lower()
spicy=spicy.lower()

if vegetarian=="yes" and spicy=="yes":
    print("Try spicy lentil curry!")
elif vegetarian=="yes" and spicy=="no":
    print("How about a vegetable lasagna?")
elif vegetarian=="no" and spicy=="yes":
    print("Spicy chicken stir fry is for you!")
elif vegetarian=="no" and spicy=="no":
    print("Classic roast beef might be good!")
else:
    print("Invalid input, please enter 'yes' or 'no'")
