% Definir numerador y denominador
num = [10 20];          % Equivale a: 10s + 20
den = [1 2 2 0];    % Equivale a: s^3 + 2s^2 + 2s + 0s + 0

% Crear la función de transferencia
G = tf(num, den);

% Calcular polos y ceros
polos = pole(G)
ceros = zero(G)

% Graficar el mapa de polos y ceros en el plano s
pzmap(G);
grid on;