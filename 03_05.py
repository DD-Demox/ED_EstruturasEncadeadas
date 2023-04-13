from filaEncadeadaProcesso import Queue

processes = Queue()
processes.push(100,"Dota2.exe",10,2)
processes.push(134,"Word",5,254)
processes.push(153,"PyCharm",9,22)
processes.push(112,"Discord",3,23)
processes.push(101,"Explorer",2,24)
processes.push(104,"Chrome",4,50)

print(processes)

processes.kill_process_highest_process_wait()
print(processes)