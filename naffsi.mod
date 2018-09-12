COMMENT
Naf model only for FSIs
implemented by HS
ENDCOMMENT

NEURON {
  SUFFIX naffsi
  USEION na READ ena WRITE ina
  RANGE gna, g
}

UNITS {
  (S) = (siemens)
  (mV) = (millivolt)
  (mA) = (milliamp)
}

PARAMETER {
  gna = 0.1125 (S/cm2)
}

ASSIGNED {
  v (mV)
  ena (mV)
  ina (mA/cm2)
  g (S/cm2)
}

STATE {
  m
  h
}

BREAKPOINT {
  SOLVE states METHOD cnexp
  g = gna * h * m^3
  ina = g * (v-ena)
}

INITIAL {
  m = alpham(v)/(alpham(v)+betam(v))
  h = alphah(v)/(alphah(v)+betah(v))
}

DERIVATIVE states {

  m' = alpham(v)*(1-m)-betam(v)*m
  h' = alphah(v)*(1-h)-betah(v)*h

}

FUNCTION alpham(v (mv)) {
	UNITSOFF
	alpham=(3020-40*v)/(exp((-75.5+v)/(-13.5))-1)
	UNITSON
}

FUNCTION betam(v (mv)) {
	UNITSOFF
	betam=1.2262/(exp(v/42.248))
	UNITSON
}

FUNCTION alphah(v (mv)) {
	UNITSOFF
	alphah=0.0035/(exp(v/24.186))
	UNITSON
}

FUNCTION betah(v (mv)) {
	UNITSOFF
	betah=-(0.8712+0.0017*v)/(exp((51.25+v)/(-5.2))-1)
	UNITSON
}

