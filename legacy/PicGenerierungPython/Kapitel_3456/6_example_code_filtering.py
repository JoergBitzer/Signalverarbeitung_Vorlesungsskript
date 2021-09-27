import numpy
InputVektor = [1, 2, 0, 0, 5]
v_Coeffs = numpy.array([1, 3, 4])
v_states = numpy.zeros((len(v_Coeffs)))
InputVektor = numpy.concatenate((InputVektor, [0]*(len(v_Coeffs)-1)))

out = []
for val in InputVektor:        # Annahme Daten stehen in InputVektor
    v_states[0] = val       # Neuen Datenwert in State speichern
    out.append(numpy.matmul(v_Coeffs, v_states))     # Skalarprodukt berechnen
    v_states[1:] = v_states[0:len(v_states)-1] # State Vector verschieben
