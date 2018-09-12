COMMENT
NAS channel only for FSIs
implemented by HS
ENDCOMMENT

NEURON {
  SUFFIX nas
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
  theta_m = -24 (mV)
  sigma_m = 11.5 (mV)
  theta_h = -58.3 (mV)
  sigma_h = -6.7 (mV)
  theta_t_h = -60 (mV)
  sigma_t_h = -12 (mV)
  taum = 0.001 (ms) : for stability with dt>0.01 ms
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
  m = minfi(v)
  h = hinfi(v)
}

DERIVATIVE states {
  m' = (minfi(v)-m)/taum
  h' = (hinfi(v)-h)/tauh(v)
}

FUNCTION hinfi(v (mV)) {
  UNITSOFF
  hinfi=1/(1 + exp(-(v-theta_h)/sigma_h))
  UNITSON
}

FUNCTION tauh(v (mV)) (ms) {
  UNITSOFF
  tauh = 0.5 + 14 / ( 1 + exp(-(v-theta_t_h)/sigma_t_h))
  UNITSON
}

FUNCTION minfi(v (mV)) {
  UNITSOFF
  minfi=1/(1 + exp(-(v-theta_m)/sigma_m))
  UNITSON
}
