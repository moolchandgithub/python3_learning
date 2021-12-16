def tax(state, income):
    """
    Calculate the tax as per state slab.
    :param state: State name
    :param income: Your income
    :return : Your calculated tax
    """
    l = {'har': 10, 'up': 15, 'del': 20}
#    for a, b in l.items():
    if state in l:
        print(f"Tax in {state} is {l[state]}%.")
        tax = (l[state] / 100)*income
        net_income = income - tax
        return tax, net_income
    else:
        print("Default tax slab is 30%")
        tax = (30 / 100)*income
        net_income = income - tax
        return tax, net_income

calculate_tax = tax('up', 1250)
print(f"You tax is: {calculate_tax[0]}.")
print(f"Your net income after tax is: {calculate_tax[1]}.")

#help(tax)