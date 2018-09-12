COMMENT
KV channel only for FSIs
implemented by HS
ENDCOMMENT

NEURON {
  SUFFIX kv
  USEION k READ ek WRITE ik
  RANGE gkv, g
}

UNITS {
  (S) = (siemens)
  (mV) = (millivolt)
  (mA) = (milliamp)
}

PARAMETER {
  gkv = 0.225 (S/cm2)
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
  g = gkv * n^2
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
	alphan=(95-v)/(exp((-95+v)/(-11.8))-1)
	UNITSON
}

FUNCTION betan(v (mv)) {
	UNITSOFF
	betan=0.025/(exp(v/22.222))
	UNITSON
}
