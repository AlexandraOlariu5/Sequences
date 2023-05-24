available_parts = [("computer", 200),
                   ("monitor", 100),
                   ("keyboard", 50),
                   ("mouse", 30),
                   ("mouse mat", 15),
                   ("hdmi cable", 20),
                   ("dvd drive", 25)
                   ]

valid_choices = []
choice = "-"
basket = []
total_price = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

while choice != "0":
    if choice in valid_choices:
        index = int(choice) - 1
        chosen_part = available_parts[index]

        if chosen_part[0] in basket:
            print("Are you sure you want to add this item again?")
            options = input("YES/ NO ")
            print()

            if options == "Yes".casefold():
                basket.append(chosen_part[0])
                total_price.append(chosen_part[1])
                print()

            elif options == "No".casefold():
                print("You won't add {} to your basket one more time."
                      .format(chosen_part[0]))

        else:
            basket.append(chosen_part[0])
            total_price.append(chosen_part[1])
            print("You chose: {}".format(chosen_part[0]))
            print("This item costs: £{}".format(chosen_part[1]))
            print()

        print(basket)
        print(total_price)
        print()
    elif choice == 0:
        break

    else:
        print("Please choose from our range: ")
        print()
        for index, (part, price) in enumerate(available_parts):
            print("{}: {} - {}".format(index + 1, part, price))
        print()
    choice = input("What would you like to buy today? "
                   "\nChoose from our options: ")
print()
print(basket)
print("TOTAL TO PAY: {}".format(sum(total_price)))