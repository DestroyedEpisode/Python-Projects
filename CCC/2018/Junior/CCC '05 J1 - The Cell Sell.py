plan_a = {
	"day" : 0.25,
	# 25 cents per minute
	"eve" : 0.15,
	# 15 cents per minute
	"week" : 0.2,
	# 20 cents per minute
	"free" : 100
}
plan_b = {
	"day" : 0.45,
	# 45 cents per minute
	"eve" : 0.35,
	# 35 cents per minute
	"week" : 0.25,
	# 25 cents per minute
	"free" : 250
}

d = int(input())
e = int(input())
w = int(input())

def charge_a():
	if d > plan_a['free']:
		return round(((d - plan_a["free"]) * plan_a["day"]) + (e * plan_a["eve"]) + (w * plan_a["week"]), 2)
	else:
		return round((e * plan_a["eve"]) + (w * plan_a["week"]), 2)

def charge_b():
	if d > plan_b['free']:
		return round(((d - plan_b["free"]) * plan_b["day"]) + (e * plan_b["eve"]) + (w * plan_b["week"]), 2)
	else:
		return round((e * plan_b["eve"]) + (w * plan_b["week"]), 2)

print('Plan A costs', charge_a())
print('Plan B costs', charge_b())

if charge_a() > charge_b():
	print('Plan B is cheapest.')
elif charge_a() < charge_b():
	print('Plan A is cheapest.')
elif charge_a() == charge_b():
	print('Plan A and B are the same price.')
