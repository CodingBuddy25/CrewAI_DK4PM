def update_event_log(agent_name, agent_research):
    output_file = open(f"event_log.txt", "w")
    to_write = f"""\n ________________{agent_name}_______________ \n {agent_research}
___________END______________"""
    output_file.write(to_write)
    output_file.close()

def read_event_log():
    output_file = open("event_log.txt", "r")
    read_file = output_file.read()
    output_file.close()
    return read_file
