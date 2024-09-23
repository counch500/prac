a = int(input())
match a:
	case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case chet if (chet%2) == 0:
        print("Chetnoe")
    case nechet:
        print(nechet, "--это много")
