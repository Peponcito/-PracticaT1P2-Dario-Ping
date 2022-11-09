# PracticaT1P2-Dario-Ping
> En esta práctica se nos pedía desarollar una aplicación utilizando python que ejecute el comando ping que sirve para ver si 
una máquina está activa dentro de una red y devuelva el resultado por pantalla.
### Funcioanmiento de del programa:
- Cree una funcion llamada ping, a la cula le tnemos que pasar un parámetro, el cual yo llame host.
- Dentro de la función ping se crean 2 varaibles, una llamada parametro y otra llamada comando.
  - *parametro:* Le indico el parámetro que va a introducir en el comando sea '-n' y que si el sistema es distinto de windows 
  el parámetro que introduzaca en el comnado sea '-c'
  - *comando* Le indicio cuáles los los diferentes parámetros del comando, primero le indicio que comando hay que utilizar, en este caso el ping, después, con la otra
  variable, le indicio que parámetro hay que poner, después se le indica el número de veces que se hace el ping y por último el parametro 
  host, que es la direcion ip que le queire hacer ping.
- Por último se llama al funcion call del subproces y se le pasa el comando
