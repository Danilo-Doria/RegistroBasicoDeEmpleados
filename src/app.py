import employees
import services

print("\nBienvenido al sistema de manejo de empleados")

option = 0

while option != 6:
    print("\n1. Agregar empleado")
    print("2. Mostrar empleados")
    print("3. Buscar empleado")
    print("4. Actualizar empleado")
    print("5. Eliminar empleado")
    print("6. Salir")

    try:
        option = int(input("\nDigite la opción que desea realizar: "))

        if option not in range(1, 7):
            print("\n Opción invalida")
            continue
    except ValueError:
        print("\nPor favor solo digite valores numericos")
        continue
    
    if option == 1:
        services.add_employee(employees.employees)
    elif option == 2:
        services.display_employees(employees.employees)
    elif option == 3:
        services.search_employee(employees.employees)
    elif option == 4:
        services.update_employee(employees.employees)
    elif option == 5:
        services.delete_employee(employees.employees)
    else:
        print("\nAdios")
        break
