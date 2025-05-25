clear;

k = 1;
n = 10;

NodeVector = linspace(0, 1, n+k+2);
Nik = zeros(n+1, 1);

for u = k/(n+k+1) : 0.001 : (n+1)/(n+k+1)
    for i = 0 : 1 : n
        Nik(i+1, 1) = BaseFunction(i, k , u, NodeVector);
    end
end

plot(Nik)