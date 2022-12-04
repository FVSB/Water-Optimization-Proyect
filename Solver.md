Instrucciones de uso:
Ejecutar el archivo test.py
Rellenar los datos de DataBase.xlsx con la forma predeterminada

Breve explicación de uso del solver
El solver utilizado para este trabajo es pulp, el cual es una biblioteca de python de código abierto que mediante LpProblem nos proporciona una manera fácil de resolver problemas de programación lineal. Para este caso en específico se utilizó ademas las LpVariable las cuales son las variables del modelo, el mismo nos proporciona la facilidad de establecer el rango mínimo y máximo de dichas variables, después poder agregar la función objetivo la cual puede tener a sus variables con operaciones, se añaden las restricciones de la función y se invoca a resolver, dado el objetivo:maximizar o minimizar este entrega el valor optimo de la función objetivo y el valor de cada variable.


Ejecutar el test.py
