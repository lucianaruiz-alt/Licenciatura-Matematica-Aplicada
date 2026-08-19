% Definir numerador y denominador
num = [10 0];          % Equivale a: 10s 
den = [1 4 4];   % Equivale a: s^2 + 4s + 4

% Crear la función de transferencia
G = tf(num, den);

% Calcular polos y ceros
polos = pole(G)
ceros = zero(G)

% Graficar el mapa de polos y ceros en el plano s
pzmap(G);
grid on;