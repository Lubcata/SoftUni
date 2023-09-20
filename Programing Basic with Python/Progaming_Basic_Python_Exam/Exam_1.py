from math import ceil

card_price = int(input())
transition_price = int(input())
voltage_cost_per_day = float(input())
profit_per_day = float(input())

number_of_cards = 13
number_of_transitions = 13
parts = 1000

card_cost = card_price * number_of_cards
transition_cost = transition_price * number_of_transitions
total_cost = card_cost + transition_cost + parts

profit_card_per_day = profit_per_day - voltage_cost_per_day
total_profit_card_per_day = number_of_cards * profit_card_per_day
days_to_return = ceil(total_cost / total_profit_card_per_day)

print(total_cost)
print(days_to_return)
