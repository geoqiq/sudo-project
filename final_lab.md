
### Curs 7
* baza este codul de la curs
* actualizam separat pitch si velocity
* putem sa incercam sa actualizam separat si yaw
* yaw cu valori pozitive -> stanga, altfel spre dreapta
* ne asiguram ca atunci cand robotul nu mai vede mingea, revine la pozitie neutra si se opreste

### Curs 8
* primul pas verificam daca se vede sau nu mingea (center is None)
* pitch pentru a asigura echilibrul il pastram in [-10,10]
* cand este destul de aproape de minge (radius>100) setam pitch la -20 pentru a orienta fata robotului la maxim de jos
* asa va continua sa vada mingea
* cand radius e in intervalul [50, 100], punem velocity mai mic pentru a se apropia cu pasi mai marunti de minge
* dupa ce suntem langa minge, facem:
  
```
    yaw la 10 grade
    pas inainte cu velocity 6
    timp de 2 secunde
```

```stop all movement```

```
  kick cu piciorul drept
  action_srv("kick_ball_right.d6ac", True) // default
  SAU
  action_srv("my_kick.d6ac", True)         // custom
```

```time.sleep(3) // mai mult decat dureaza secventa de kick```

* True din action_srv ne spune ca actiunea se face secvential
* in loc de un cadran central pe ecran in care vrem sa avem mingea, il vom shifta spre dreapta pentru a ne asigura ca mingea ramane langa picior
* colt stanga sus [320,180] si colt dreapta jos [480,300]
* putem schimba gate intr-unul mai stabil: 0.15, 0.15 si 0
* multe valori ajustate experimental, eventual incercati sa rezolvati ca aluneca robotul pe jos (ii punem botosei?)
* cursul 8 cu o varianta in care toate tipurile de miscari yaw, pitch, velocity erau tratate separat si nu erau modificate deodata (folosim niste bool pentru a tine socoteala)

#### Kick custom
0. deschidem aplicatia cu portocaliu de pe desktop (schimbam limba tab stanga in engleza)
1. setam pentru picioarele din spate z la -8 (0.5sec)
2. front_right z=-7 (0.5sec)
3. front_right x=11 (0.5sec) - se mai poate ajusta experimental
4. reset la valori initiale
5. save action file (in pi/PuppyPi_PC_Software/ActionGroups)

* pentru un kick mai violent o sa setam un timp mai mic la pasul 3
