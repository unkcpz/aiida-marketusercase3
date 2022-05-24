header_template = """#include "udf.h"
#include "math.h"

#define R 8.314											/* J/m/K */

/* Catalyst properties*/
#define A0 {A0}							/* ***USER INPUT*** Initial active surface area (m2/g active material)*/
#define X_pd {X_pd}						/* ***USER INPUT*** Mass fxABJSraction of active material */

/* Set reaction rate parameters*/
#define k0 {k0}						/* ***USER INPUT*** Pre-exponential factor*/
#define Ea {Ea}						/* ***USER INPUT*** Activation energy (J/mol) */

/* Support particle properties*/
#define por_cat {por_cat}					/* ***USER INPUT*** Catalyst support macroporosity*/
#define tort {tort}						/* ***USER INPUT*** Macropore tortuosity */
#define rp {rp}						/* ***USER INPUT*** Macropore average radius (nm)*/
"""

journal_template ="""/file/read-case-data FSP-Lurederra_alumina-end
/file/read-macros "postintime-FSP-Lurederra_alumina.scm"
(rpsetvar 'flow-time 0)
(rpsetvar 'time-step 0)

;Run simulation with stabilized flame
; Set operating conditions

/define/models/dpm/injections/set-injection-properties spray spray no no no particle_injection () no no yes no 1 0.15 no no no no no no {Xylenemf} c8h10gas {ATSBmf} c12h27alo3gas {Precvel} 0 {Dropsmd} 298 0 100 {Precmfr}
;																	xylene mf      ASB mf              velocity diameter           mass flow
/define/boundary-conditions/mass-flow-inlet dispersion yes yes no {Dispmfr} no 300 no 0 no yes no no yes 5 10 no no 0 no 0 no 0 no 1 no 0 no 0 no 0 yes no 1 no yes no yes no yes yes yes "udf" "N_boundary::FSP" yes yes "udf" "A_boundary::FSP" yes yes "udf" "V_boundary::FSP" no yes
;                                                                mass flow rate
/define/boundary-conditions/mass-flow-inlet pilot_fuel yes yes no {Pilotmfr} no 300 no 0 no yes no no yes 5 10 no no 0 no {Pilotch4mf} no 0 no {Piloto2mf} no 0 no 0 no 0 yes no 1 no yes no yes no yes yes yes "udf" "N_boundary::FSP" yes yes "udf" "A_boundary::FSP" yes yes "udf" "V_boundary::FSP" no yes
;                                                                mass flow rate                                     CH4 mass fraction  O2 mass fraction
/define/boundary-conditions/mass-flow-outlet outlet yes yes no {Fanextrate} no yes 300 no 1 no yes no yes no yes yes yes "udf" "N_boundary::FSP" yes yes "udf" "A_boundary::FSP" yes yes "udf" "V_boundary::FSP" no
;                                                            mass flow rate  


/solve/set/max-flow-time 1e-4
/solve/set/time-step 5e-6
/solve/dual-time-iterate 20 10

/file/write-case-data FSP-Lurederra_alumina-end2
"""