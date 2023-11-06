from OOP import Car #what you are doing here is mentiong the name of the module after from and then after import name of the class

car_1 = Car("chevy", "corvetter", 2021, "blue")
car_2 = Car("Ford", "Mustange", 2022, "Yellow"
)
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)



car_1.drive() # here we are basically calling methods we have created in OOP module
car_1.stop()


print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()

#in python for self we do not need to pass in anything
