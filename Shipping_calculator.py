premium_shipping = 125    

def ground_shipping(weight):
	if weight <= 0:
		return "Weight cannot be equal or smaller than 0"
	elif weight <= 2:
		return weight * 1.50 + 20
	elif weight > 2 and weight <= 6:
		return weight * 3 + 20
	elif weight > 6 and weight <= 10:
		return weight * 4 + 20
	elif weight > 10:
		return weight * 4.75 + 20
	
print(ground_shipping(10))

def drone_shipping(weight):
	if weight <= 0:
		return "Weight cannot be equal or smaller than 0"
	elif weight <= 2:
		return weight * 4.50
	elif weight > 2 and weight <= 6:
		return weight * 9 
	elif weight > 6 and weight <= 10:
		return weight * 12
	elif weight > 10:
		return weight * 14.25
	
print(drone_shipping(1.5))  

def price_compare(weight):
	if weight <= 0:
		return "Weight cannot be equal or smaller than 0"
	if drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_shipping:
		return "Shipping by drone is cheaper! Total cost:" + str(drone_shipping(weight))
	if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_shipping:
		return "Shipping by ground is chaper! Total cost:$" + str(ground_shipping(weight))
	if premium_shipping < drone_shipping(weight) and premium_shipping < ground_shipping(weight):
		return "The best option is using Premium Shipping, at a cost of $"+ str(premium_shipping)
	if drone_shipping(weight) == ground_shipping(weight):
		return "Either Drone or Ground shipping cost the same:$"+ str(ground_shipping(weight))
	if drone_shipping(weight) == premium_shipping:
		return "Either Drone or Premium Shipping cost the same:$" + str(drone_shipping(weight))
	if premium_shipping == ground_shipping(weight):
		return "Either Premium or Ground shipping cost the same:$" + str(ground_shipping(weight))
	if premium_shipping == ground_shipping(weight) and ground_shipping(weight) == drone_shipping(weight):
		return "Bullseye!!! All options would cost exacly the same:$" + str(ground_shipping(weight))
	
print(price_compare(20))  

	

