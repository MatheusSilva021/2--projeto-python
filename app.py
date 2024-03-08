from models.restaurant import Restaurant

restaurante1 = Restaurant('Madero','Hambúrguer')
restaurante1.activate_restaurant()
restaurante1.add_rating('Cliente_1',3)
restaurante1.add_rating('Cliente_2',5)
restaurante1.add_rating('Cliente_3',2)

def main():
    Restaurant.show_restaurants()

if __name__ == "__main__":
    main()