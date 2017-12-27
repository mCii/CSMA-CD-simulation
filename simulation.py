import numpy as np
import random
import matplotlib.pyplot as plt

def draw(a,b,c):
	plt.plot(a, b, 'ro')
	plt.axis([0,c+1 , 0, 100])
	plt.show()

def create(nb_packets,max_random):
	array=[]
	index=[]
	nb_collisions=[]
	packets_arrival=[]
	for i in range(nb_packets):
		index.append(i+1)
		nb_collisions.append(0)
	a=list(range(max_random))
	a=[x+1 for x in a]
	np.random.shuffle(a)
	for i in range(nb_packets):
		packets_arrival.append(a[i])
	packets_arrival.sort()
	array.append(np.array(index))
	array.append(np.array(packets_arrival))
	array.append(np.array(packets_arrival))
	array.append(np.array(nb_collisions))
	return array


def Main():
#generation des random dates des packets
	number_machine_max = int(input("Donnez le nombre de machines maximal:	"))
	machines=list(range(number_machine_max))
	machines=[c+1 for c in machines]
	taux_erreur=[]
	for i in range(len(machines)):
		nb_collusions=0
		t=[]
		temps=1
		for w in range(machines[i]):
			temp_array=create(3,10)    #creation de 3 packets a temps maximal 10 pour chaque machine des N
			t.append(temp_array)
		print("************************************************************************************")
		print("debut log pour n =", machines[i], "machines")
		print("Voici les temps d'arrivées aléaoires")
		for k in range(len(t)):
			print("machine", k+1)
			print(t[k][2])
		while (True):
			s=[]
			hosts=[]
			h=0
			for i in range(len(t)):
				if np.size(t[i]) > 0:    #si la machine i possede des packets
					if t[i][1][0] == temps:	 #comparaion non temps
						s.append(t[i][1][0])
						hosts.append(i)	
				else:
					h=h+1
			if h==len(t):		#si toutes les machine n'ont pas des packets
				break
		#	print(t)
			if len(s)==0:		#aucune machine va transmettre
				print("temps: " + str(temps) + " *** " + "Pas de packets")
				temps+=1
			elif len(s)==1:		#une seule machine va transmettre
				print("date d'émission:" + str(temps) + " *** " + "Machine:" + str(hosts[0]+1) + " *** " + "packet:" + str(t[hosts[0]][0][0]) +" *** " + "date arrivée:" + str(t[hosts[0]][2][0]))
				temps+=1
				t[hosts[0]]=np.delete(t[hosts[0]],0,1) #depiler le packet
				if np.size(t[hosts[0]]) > 0:	#si la machine possede de plus des packets apres depilation
					if t[hosts[0]][1][0]<temps: # si le temps depasse la date du packet
						t[hosts[0]][1][0]=temps
				
			else :					#collision
				print("temps:", str(temps) , "***" , "Collision entre: ", end='*')
				nb_collusions+=1
				for h in range(len(hosts)):
					print("machine",hosts[h]+1,end='*')
				print()
					
				rands=[]
				for j in range(len(hosts)):
					t[hosts[j]][3][0]+=1												#incrementer le nombre de collisions pour le packet
					rand=random.choice(list(range(pow(2,t[hosts[j]][3][0]))))  			#random time slot waiting
					t[hosts[j]][1][0]+=rand												#incrementer temps d'emission du packet
					rands.append(rand)													
					print("machine", hosts[j]+1, "attend", rand, "time slots")
		# siaucune machine va envoyer directement on incremente le temps	
				if rands.count(0) == 0:													
					temps+=1	
				print("******************************************\n")
		print("fin log pour n=", machines[i],"machines")
		print("*************************************************************************************")
		collusion_var=nb_collusions*100/(3*machines[i])
		collusion_var="%.2f" % collusion_var
		collusion_var=float(collusion_var)
		taux_erreur.append(collusion_var)
	print(machines)
	print(taux_erreur)
	draw(machines,taux_erreur, number_machine_max)
if __name__ == '__main__':
	Main()