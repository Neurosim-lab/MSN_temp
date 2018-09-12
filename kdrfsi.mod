COMMENT
FSI Kdr channel (used only for FSI)
implemented by HS

ENDCOMMENT

NEURON {
  SUFFIX kdrfsi
  USEION k READ ek WRITE ik
  RANGE gkdr, g
}

UNITS {
  (S) = (siemens)
  (mV) = (millivolt)
  (mA) = (milliamp)
}

PARAMETER {
  gkdr = 0.0529 (S/cm2)
}

ASSIGNED {
  v (mV)
  ek (mV)
  ik (mA/cm2)
  g (S/cm2)
}

STATE {n}

BREAKPOINT {
  SOLVE states METHOD cnexp
  g = gkdr * n^4
  ik = g * (v-ek)
}

INITIAL {
  n = alphan(v)/(alphan(v)+betan(v))
}

DERIVATIVE states {

  n' = alphan(v)*(1-n)-betan(v)*n

}

FUNCTION alphan(v (mv)) {
	UNITSOFF
	alphan=-(0.616+0.014*v)/(exp((44+v)/(-2.3))-1)
	UNITSON
}

FUNCTION betan(v (mv)) {
	UNITSOFF
	betan=0.0043/(exp((44+v)/34))
	UNITSON
}

