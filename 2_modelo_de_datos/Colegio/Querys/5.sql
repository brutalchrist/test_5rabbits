select c.t_nombre as "Curso", concat(p.t_nombre, p.t_apellido1) as "Alumno", ROUND(avg(n_nota), 2) as "Promedio"
from ALUMNO a
join PRUEBA_X_ALUMNO pa 
	on pa.pers_x_pers = a.x_pers
join PRUEBA pr 
	on pr.x_prue = pa.prue_x_prue
join PERSONA p 
	on p.x_pers = pa.pers_x_pers
join CURSO c 
	on c.x_curs = pr.curs_x_curs
group by pa.pers_x_pers, pr.curs_x_curs
HAVING ROUND(avg(n_nota), 2) < 4.0;