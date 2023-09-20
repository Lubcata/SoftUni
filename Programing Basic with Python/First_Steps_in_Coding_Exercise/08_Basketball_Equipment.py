# • Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

# · Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999

year_fee = int(input())
sneakers_price = year_fee - (year_fee * 0.40)
clothes_price = sneakers_price - (sneakers_price * 0.20)
ball_price = clothes_price / 4
accessorie_price = ball_price / 5

expenses = year_fee + sneakers_price + clothes_price +  ball_price + accessorie_price

print(expenses)