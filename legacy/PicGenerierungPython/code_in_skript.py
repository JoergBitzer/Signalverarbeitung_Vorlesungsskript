import numpy
LengthOfFilter = 10
InputVektor = [1, 2, -2, -1]


# 6.1.3.1
v_states = numpy.zeros(LengthOfFilter,1);

for kk = 1:length(InputVektor) % Annahme Daten stehen in InputVektor
v_states(1) = InputVektor(kk); % Neuen Datenwert in State speichern
out(kk) = v_Coeffs.’ * v_states; % Skalarprodukt berechnen
v_states(2:end) = v_states(1:end-1); % State Vector verschieben
end

#