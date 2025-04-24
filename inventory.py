import random

p = [125, 125, 150, 175, 175]  
q = [150, 250, 250, 250, 300]  
cost = [0] * 5  

for policy in range(5):  
    stock = 115  
    duedate = 0  
    unitsdue = 0  
    day = 1  

    for day in range(1, 181):  # Simulate for 180 days
        if day == duedate:
            stock += q[policy]  
            unitsdue = 0

        demand = random.randint(0, 99)  

        if demand <= stock:
            stock -= demand  
            carrying = stock * 0.75  
            cost[policy] += carrying
        else:
            left = demand - stock  
            stock = 0  
            shortage = left * 18  
            cost[policy] += shortage

        # Check if we need to reorder
        if stock + unitsdue <= p[policy]:  
            unitsdue = q[policy]  
            reorder_cost = 75 
            cost[policy] += reorder_cost  
            duedate = day + 3  

    # After the 180 days, print the total cost for this policy
    print(f"Total cost for policy {policy + 1} (p={p[policy]}, q={q[policy]}): {cost[policy]}")

