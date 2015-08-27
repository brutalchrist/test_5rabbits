# Players Tenis

## Respuesta

La respuesta es: 190. 

La consulta sin la condición where lo que hace es hacer la combinación de cada uno de player con todos los players. Por ejemplo:

N     | c1.Ranking | c2.Ranking
------|------------|-----------
1     | 42         | 42
2     | 89         | 42 
3     | 78         | 42
[...] | [...]      | [...]
20    | 23         | 42
21    | 42         | 89
22    | 89         | 89 
23    | 78         | 89
[...] | [...]      | [...]
40    | 23         | 89

Si ordenamos estos resultados de menor a mayor nos daremos cuenta que el más pequeño de los c2 19 números serán mayor que el, el siguiente c2 18 números serán mayor que el y así hasta el mayor de los c2 que tendrá 0 números mayores que él. A continuación ejemplo (simple) del primer y último pack:

Pack: 1

c1 | c2 | c1 > c2
---|---|---
1 | 1 | False
2 | 1 | True
3 | 1 | True
4 | 1 | True
5 | 1 | True
6 | 1 | True
7 | 1 | True
8 | 1 | True
9 | 1 | True
10 | 1 | True
11 | 1 | True
12 | 1 | True
13 | 1 | True
14 | 1 | True
15 | 1 | True
16 | 1 | True
17 | 1 | True
18 | 1 | True
19 | 1 | True
20 | 1 | True


Pack: 20

c1 | c2 | c1 > c2
---|---|---
1 | 20 | False
2 | 20 | False
3 | 20 | False
4 | 20 | False
5 | 20 | False
6 | 20 | False
7 | 20 | False
8 | 20 | False
9 | 20 | False
10 | 20 | False
11 | 20 | False
12 | 20 | False
13 | 20 | False
14 | 20 | False
15 | 20 | False
16 | 20 | False
17 | 20 | False
18 | 20 | False
19 | 20 | False
20 | 20 | False

Esto es como el problema de la suma de N primeros números de Gauss. La resolución sería:
``` math
  19 + 18 + 17 + ... + 0  # La suma que debemos realizar 
  19 + 0 = 19             # Según Gauss podemos sumar el primer y el último dígito
  19 * 10 = 190           # Y multiplicarlo por el numero de operatorias (numero total de numeros dividido 2)
```


## Probar

### Crear tabla

``` sql
CREATE TABLE IF NOT EXISTS `PLAYERS` (
  `Nombre` varchar(150) NOT NULL,
  `Pais` varchar(150) NOT NULL,
  `Ranking` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```
### Ejecutar script

    $ python generadorInsert.py

Al ejecutar el script generadorInsert.py se creará un archivo insertPlayers.sql con 20 inserts de Players con Rankings aleatorios únicos (1 - 100).

### Consulta SQL
``` sql
SELECT count(1)
FROM PLAYERS c1, PLAYERS c2  
WHERE c1.Ranking > c2.Ranking
```
