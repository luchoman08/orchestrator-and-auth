import itertools, string, re
from pulp import *
from time import time


def resolverProblemaEquilibrio(agente_horas, tarea_costo):
    agentes = agente_horas.keys()
    tareas = tarea_costo.keys()
    tareasxagente = list(itertools.product(agente_horas.keys(), tarea_costo.keys())) # Lista de pares resultante de hacer producto cartesiano entre agentes y tareas 
    prob = pulp.LpProblem("Equilibrio de asignaciones", pulp.LpMinimize) 
    variables_asignacion = pulp.LpVariable.dicts("Asignacion",tareasxagente,None,None,pulp.LpBinary)
    #Variables auxiliares para ayudarse a resolver la desviacin estandard
    aux_vars = pulp.LpVariable.dicts("Auxiliar", [(a, "temporal") for a in agentes], None, None)
    #Funcion objetivo
      
    
    
    def construir_funcion_objetivo(agentes):
        return pulp.lpSum(aux_vars)
    
    
    prob += construir_funcion_objetivo(agentes), "Minimizar desviacion estandard de el trabajo"
    
    porcentaje_uso_tiempo_agentes = {}
    cargas_por_agente = {}
    
    
    for agente in agentes:
    	cargas_por_agente[agente] = [tarea_costo [i[1]] * variables_asignacion[i] for i in tareasxagente if i[0] == agente]
     
    
    for agente in agentes:
    	porcentaje_uso_tiempo_agentes[agente] = pulp.lpSum([x * 100 / agente_horas[agente] for x in cargas_por_agente[agente] ])
    
    promedio_porcentaje_uso_tiempo_agentes_exepto_agente = {}
    
    porcentaje_uso_tiempo_agentes_menos_porcentaje_uso_tiempo_agente_dividido_longitud_agentes = {}
    for agente in agentes:
    	porcentaje_uso_tiempo_agentes_menos_porcentaje_uso_tiempo_agente_dividido_longitud_agentes[agente] =	porcentaje_uso_tiempo_agentes[agente] - porcentaje_uso_tiempo_agentes[agente]  / len(agentes)
    
    for agente in agentes:
    	promedio_porcentaje_uso_tiempo_agentes_exepto_agente[agente] = \
    	(-pulp.lpSum([porcentaje_uso_tiempo_agentes[agentex] \
    	for agentex in agentes if agentex != agente]) /  len(agentes)) + porcentaje_uso_tiempo_agentes_menos_porcentaje_uso_tiempo_agente_dividido_longitud_agentes[agente]
    
    
    #Restricciones
    
    #La suma de las horas asignadas no puede superar el mximo de horas disponibles
    for agente in agentes:
    	prob +=  pulp.lpSum(cargas_por_agente[agente]) <= agente_horas[agente]
        
    #Una tarea solamente puede ser asignada a una persona:
    
    for tarea in tareas:
    	prob+= pulp.lpSum([variables_asignacion[i] for i in tareasxagente if i[1] == tarea]) == 1
    	
    
    for agente in agentes:
        prob += promedio_porcentaje_uso_tiempo_agentes_exepto_agente[agente] <= aux_vars[(agente, 'temporal')]
        prob += promedio_porcentaje_uso_tiempo_agentes_exepto_agente[agente] >= - aux_vars[(agente, 'temporal')]
    #prob.writeLP("EquilibrioTrabajo.lp")
    
    tiempo_solve_inicial = time() 
    prob.solve()
    tiempo_final_solve = time() 
    
    
    tiempo_solve = tiempo_final_solve - tiempo_solve_inicial
    
    # The status of the solution is printed to the screen
    print("Status:", pulp.LpStatus[prob.status])
    
    for v in prob.variables():
        print(re.findall(r'\d+', v.name))
        print(v.name, "=", v.varValue)
    
    
    print ('El tiempo total de el solve fue:', tiempo_solve) #En segundos 
    