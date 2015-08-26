select P.* 
from CURSO C
join CURSO_X_ALUMNO CU
    on C.X_CURS = CU.CURS_X_CURS
join PERSONA P
    on CU.PERS_X_PERS = P.X_PERS
where
    C.T_NOMBRE = "programación"