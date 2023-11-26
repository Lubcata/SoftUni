def add_stop(stops, index, string):
    if index in range(len(stops)):
        stops = stops[:index] + string + stops[index:]
    return stops 


def remove_stop(stops, start_index, stop_index):
    if start_index in range(len(stops)) and stop_index in range(len(stops)):
        stops = stops[:start_index] + stops[stop_index + 1:]
    return stops    
        
 
def switch(stops, old_string, new_string):
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops
        

def main():
    
    stops = input()

    while True:
        command = input().split(":")
        action = command[0]
        if action == "Travel":
            break
        
        elif action == "Add Stop":
            index = int(command[1])
            string = command[2]
            stops = add_stop(stops, index, string)
        
        elif action == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])
            stops = remove_stop(stops, start_index, end_index)
        
        elif action == "Switch":
            old_string = command[1]
            new_string = command[2]
            stops = switch(stops, old_string, new_string)
            
        print(stops)
    
    print(f"Ready for world tour! Planned stops: {stops}")       
main()