select ROUND(AVG(PA.N_NOTA), 2) as "Promedio"
from PRUEBA P
join PRUEBA_X_ALUMNO PA
    on P.X_PRUE = PA.PRUE_X_PRUE
join CURSO C
    on C.X_CURS = P.CURS_X_CURS
where
    PA.PERS_X_PERS = 3 and C.X_CURS = 1