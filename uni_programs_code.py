with open("university_programs.txt") as file_in:
    file_in.readline()
    for line in file_in:
        line = line.split(":")
        information = line[0]
        
        info = information.split(",  ")
        name = info[0]
        if name[0] != "U":
            name = name.replace("University", "")
        city = info[1]
        province = info[2]
        
        programs = line[1]
        programs = programs.split(" , ")

        for program in programs:
            each_list = []
            each_list.append(name)
            each_list.append(city)
            each_list.append(province)
            each_list.append(program)
            print(each_list)
