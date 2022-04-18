@sims4.commands.Command('careerhack', command_type=sims4.commands.CommandType.Live, console_type=sims4.commands.CommandType.Cheat)
def achivementhack(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    sim = services.get_active_sim()
    output("selected " + sim.first_name + " " + sim.last_name + ".")
    careerlist = []
    careerlist = CareerService.get_career_list(CareerService)
    for career in careerlist:
        output("[" + str(careerlist.index(career)) + "] " + str(career))
@sims4.commands.Command('careeradd', command_type=sims4.commands.CommandType.Live, console_type=sims4.commands.CommandType.Cheat)
def achivementhack2(id:int,_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    careerlist = CareerService.get_career_list(CareerService)
    sim = services.get_active_sim()
    output("selected " + sim.first_name + " " + sim.last_name + ".")
    if id < len(careerlist):
        sim.sim_info.career_tracker.add_career(careerlist[id](sim.sim_info))
    else:
        output("Error!You didnt use careerhack command or the career is not found! career len is " + str(len(careerlist)))
