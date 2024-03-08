import numpy as np
fuel_efficiency = np.array([25, 30, 28, 32, 27, 26, 29])
average_fuel_efficiency = np.mean(fuel_efficiency)
print(f"The average fuel efficiency is: {average_fuel_efficiency} miles per gallon")
car_model_1 = 2  
car_model_2 = 5 
fuel_efficiency_improvement = ((fuel_efficiency[car_model_2] - fuel_efficiency[car_model_1]) / fuel_efficiency[car_model_1]) * 100
print(f"The percentage improvement in fuel efficiency between car model {car_model_1} and car model {car_model_2} is: {fuel_efficiency_improvement}%")
