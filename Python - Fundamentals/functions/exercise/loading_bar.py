def loading_bar(percent):
    if percent == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        percentage = (percent//10) * "%"
        dots = (10 - (percent//10)) * "."
        print(f"{percent}% [{percentage}{dots}]")
        print("Still loading...")


current_percent = int(input())
loading_bar(current_percent)
