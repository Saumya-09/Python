import psutil
def getListOfProcessSortedByMemory():
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
        try:
            # Fetch process details as dict
            pinfo = proc.as_dict(attrs=['name'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            # Append dict to list
            listOfProcObjects.append(pinfo);
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listOfProcObjects


def main():
    print()

    listOfRunningProcess = getListOfProcessSortedByMemory()

    for elem in listOfRunningProcess[:]:
        print(elem)


if __name__ == '__main__':
    main()