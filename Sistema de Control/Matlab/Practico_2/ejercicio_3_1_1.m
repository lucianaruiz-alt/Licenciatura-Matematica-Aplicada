% Definir numerador y denominador
num = [10 20];          % Equivale a: 10s + 20
den = [1 11 10 0 0];    % Equivale a: s^4 + 11s^3 + 10s^2 + 0s + 0

% Crear la función de transferencia
G = tf(num, den);

% Calcular polos y ceros
polos = pole(G)
ceros = zero(G)

% Graficar el mapa de polos y ceros en el plano s
pzmap(G);
grid on;
