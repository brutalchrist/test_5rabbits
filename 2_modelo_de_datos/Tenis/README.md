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

Si ordenamos estos resultados estos resultados de menor a mayor nos daremos cuenta que el más pequeño de los numeros tendrá 0 resultados, el siguiente 1 resultados, el siguiente 2 y así hasta el 
es como la suma de los N primeros (de Gauss) pero eliminando los extremos. Esto sería:


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
