from utils.parser import Weather


if __name__ == '__main__':
	user = Weather()
	print(user.weather_now(city='Батайск'))
	print(user.weather_forecast(amount_day='5', city='Moscow'))
