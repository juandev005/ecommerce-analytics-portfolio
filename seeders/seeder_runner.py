from  .base import get_seeders, set_seeder_done, get_seeders_done


def seeding_seeder(name):

    seeders = get_seeders()
    pending_dependencies = []

    if name in seeders.keys():

        for dependency in seeders[name].dependencies:
            if not get_seeders_done().get(dependency):
                pending_dependencies.append(dependency)

        if pending_dependencies:
            e = f"Los seeders [{', '.join(pending_dependencies)}] son dependientes de {name} y no fueron ejecutados\n\nPuede que tambien falte seeders de mayor prioridad**"
            return print(e)

        seeders[name].execute()
        return print(f"Seeder {name} ejecutados con exito")


    return print(f"No se encontro el seeder {name}")


def seeding_seeder_with_dependencies(name):

    seeders = get_seeders()
    pending_dependencies : dict[int , list] = {}

    if name in seeders.keys():

        for dependency in seeders[name].dependencies:
            if not get_seeders_done().get(dependency):
                priority = seeders[dependency].priority

                if not pending_dependencies or not priority in pending_dependencies.keys() :
                    pending_dependencies[priority] = []


                pending_dependencies[priority].append(seeders[dependency].name)


        if pending_dependencies:

            pending_dependencies =  dict(sorted(pending_dependencies.items()))

            for priority in pending_dependencies.values():
                for seeder in priority:
                    seeding_seeder_with_dependencies(seeder)

        seeders[name].execute()
        return print(f"Seeder {name} ejecutados con exito\nDependencias generadas: {seeders[name].dependencies}\n\n")

    return print(f"No se encontro el seeder {name}")


def seeding_all ():
    seeders = get_seeders()
    for seeder in seeders.keys():
        seeding_seeder_with_dependencies(seeder)
seeding_seeder("usuarios")