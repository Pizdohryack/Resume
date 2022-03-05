class Restaurant():

    def __init__(self,restaurant_name, cuisine_type, opened):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.opened = opened


    def describe_restaurant(self):
        print (f"{self.restaurant_name} один из лучших ресторанов в городе")
        print (f"Повара готовят кухню типа {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} сейчас {self.opened}")


class IceCreamStand (Restaurant):

    def __init__(self, restaurant_name, cuisine_type, opened):
        super().__init__(restaurant_name, cuisine_type, opened)


    def flavors1(self):

        for flavor in self.flavors:
            print(f"В ресторане {self.restaurant_name} подают мороженое {flavor}")


rest1 = IceCreamStand ('Клод Монэ', 'Киоск с мороженым', 'Открыт')
rest1.flavors = ['Ванильное', 'Шоколадное', 'С шоколадной крошкой']

rest1.flavors1()
