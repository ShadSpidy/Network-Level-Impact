# Network-Level-Impact

print("Welcome to Network Level Impact Calculator!!\nBy : Shadman")

total_traffic = float(input("Enter the Total Traffic: "))
impacted_node_traffic = float(input("Enter the Traffic catered by impacted nodes: "))

percentage_impact = float(input("Enter the current percentage impact (%): ")) / 100

NW_level_impact = ((impacted_node_traffic / total_traffic)*100) * percentage_impact

print(f"Current Network Level Impact is {NW_level_impact:.2f}")