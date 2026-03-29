def add_employee(employees):
    retry = False
    while not retry:
        try:
            id = int(input("\nDigite el numero de identificación del empleado: "))

            if id < 0:
                print("\nPor favor digite numeros positivos")
            else:
                retry = True
        except ValueError:
            print("\nPor favor solo digite valores numericos")

    for employee in employees:

        if  id == employee['id']:
            print("\nEste empleado ya se encuentra registrado")
            return None
    
    name = input("\nDigite el nombre del empleado: ").strip().lower()

    retry = False
    while not retry:
        try:
            age = int(input("\nDigite la edad del empleado: "))
            salary = float(input("\nDigite el salario del empleado: "))
            if age <0 or salary < 0:
                print("\nPor favor digite numeros positivos")
            else:
                retry = True

        except ValueError:
            print("\nPor favor solo digite valores numericos")
    
    employee = {
        "id": id,
        "nombre": name,
        "edad": age,
        "salario": salary
    }
    employees.append(employee)
    print(f"\n El empleado {name} con id {id} ha sido registrado exitosamente")
    return None


def display_employees(employees):
    if not employees:
        print("\nNo hay empleados para mostrar!!")
        return None
    for employee in employees:
        print(f"id: {employee['id']} | Nombre: {employee['nombre']} | Edad: {employee['edad']} | salario: {employee['salario']}")
    return None


def search_employee(employees):
    if not employees:
        print("\nNo hay empleados para buscar!!")
        return None
    
    name = input("\nDigite el nombre del empleado: ").strip().lower()

    for employee in employees:
        if name == employee['nombre']:
            print(f"\nDatos del empleado -> id: {employee['id']} | Nombre: {employee['nombre']} | Edad: {employee['edad']} | salario: {employee['salario']}")
            return None
    else:
        print(f"\nNo se encuentra el empleado con el nombre: {name}")
    return None

def update_employee(employees):
    if not employees:
        print("\nNo hay empleados para actualizar!!")
        return None
    
    retry = False
    while not retry:
        try:
            id = int(input("\nDigite el numero de identificación del empleado a actualizar: "))

            if id < 0:
                print("\nPor favor digite numeros positivos")
            else:
                retry = True
        except ValueError:
            print("\nPor favor solo digite valores numericos")

    for employee in employees:
        if id == employee['id']:
            print(f"\nDatos actuales -> id: {employee['id']} | Nombre: {employee['nombre']} | Edad: {employee['edad']} | salario: {employee['salario']}")
            name = input("\nDigite el nombre del empleado: ").strip().lower()

            retry = False
            while not retry:
                try:
                    age = int(input("\nDigite la edad del empleado: "))
                    salary = float(input("\nDigite el salario del empleado: "))
                    if age <0 or salary < 0:
                        print("\nPor favor digite numeros positivos")
                    else:
                        retry = True

                except ValueError:
                    print("\nPor favor solo digite valores numericos")

            employee['nombre'] = name
            employee['edad'] = age
            employee['salario'] = salary
            print(f"\nDatos nuevos -> id: {employee['id']} | Nombre: {employee['nombre']} | Edad: {employee['edad']} | salario: {employee['salario']}")
            return None
    else:
        print(f"\nNo se encuentra el empleado con el id: {id}")
    return None


def delete_employee(employees):
    if not employees:
        print("\nNo hay empleados para eliminar!!")
        return None
    
    retry = False
    while not retry:
        try:
            id = int(input("\nDigite el numero de identificación del empleado: "))

            if id < 0:
                print("\nPor favor digite numeros positivos")
            else:
                retry = True
        except ValueError:
            print("\nPor favor solo digite valores numericos")
        
    for employee in employees:
        if id == employee['id']:
            employees.remove(employee)
            print(f"\nEl empleado con el id: {id} ha sido eliminado exitosamente")
            return None
    else:
        print(f"\nNo se encuentra el empleado con el id: {id}")
    return None


