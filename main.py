# This is a sample Python script.

# task1

def count_integer(numbers_lst, integer):
    counter = 0
    for x in numbers_lst:
        if x == integer:
            counter = counter + 1
    if counter == 0:
        return 42
    else:
        return counter


numbers = [1, 4, 0, 10, 15, 6, 56, 9]
print(count_integer(numbers, 7))


# task2

def list_func(numbers_list, integer):
    repl_list = []
    for x in numbers_list:
        if x == integer:
            repl_list.append(6)
        else:
            repl_list.append(x)
    copied_list = repl_list.copy()
    # reverse the list and print it to the console
    repl_list.reverse()
    print(repl_list)
    return copied_list


numbers = [1, 2, 3, 4, 4, 5, 6, 7]
print(list_func(numbers, 5))


# task3

def compare_list(list1, list2):
    commons_list = []
    for x in list1:
        for y in list2:
            if x == y:
                if not (x in commons_list):
                    commons_list.append(x)
    return commons_list


list1 = [1, 2, 3, 4, 5]
list2 = [11, 23, 23, 8, 9]
# call of the function "compare_list"
print(compare_list(list1, list2))


# task4

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


my_list = remove_duplicates(["cat", "panther", "cat", "cougar", "cat", "lion", "cat"])

print(my_list)


# task5

def dict_func(dictionary):
    if "Type" in dictionary:
        type_value = dictionary["Type"]
    else:
        type_value = "unknown type"
    if "Brand" in dictionary:
        brand_value = dictionary["Brand"]
    else:
        brand_value = "unknown brand"
    if "Price" in dictionary:
        price_value = dictionary["Price"]
    else:
        price_value = "unknown price"

    print("You have a {0} from {1} that costs {2}".format(type_value, brand_value, price_value))

    dictionary["OS"] = "Linux"
    print(dictionary)
    return dict()


my_dict = {'Type': 'Notebook', 'Brand': 'Dell', 'Price': 2000}
dict_func(my_dict)
