# Chapter 11
![image](https://github.com/rplulbi/SQA/assets/15622730/de092918-e56f-46f0-84f1-adcb57e0f504)
![image](https://github.com/rplulbi/SQA/assets/15622730/9c6aa430-bcd6-4550-87a0-98b4cc8726bb)
![image](https://github.com/rplulbi/SQA/assets/15622730/cb8c5ffd-3c90-48f8-b49f-233ad613f309)

# Quality Assurance (QA)

-		 QA as Dealing with Defect

-		 Defect Prevention

-		 Defect Detection and Removal

-		 Defect Containment

# Defect vs. QA

-	QA: quality assurance

	-   focus on correctness aspect of Quality
	-   QA as dealing with defects

	    -  post-release: impact on consumers
	    -  pre-release: what producer can do

	-   what: testing & many others
	-   when: earlier ones desirable (lower cost) but may not be feasible
	-   how => classification below

-	How to deal with defects:

	-   prevention
	-   removal (detect them first)
	-   containment


# QA Classification

![image](https://github.com/rplulbi/SQA/assets/15622730/3a46441b-7aea-4d85-8043-d571b1e1fd3d)

-	Fig 3.1 above (p.30): QA as barriers

	-   dealing with errors, faults, or failures
	-   removing or blocking defect sources
	-   preventing undesirable consequences

# Error/Fault/Failure & QA

-	Preventing fault injection

	-	error blocking (errors, not faults)
	-	error source removal

-	Removal of faults (pre: detection)

	-	inspection: faults discovered/removed
	-	testing: failures trace back to faults

-	Failure prevention and containment:

	-	local failure, not global failure
		via dynamic measures to tolerate faults

	-	failure impact, not safety assurance


# Defect Prevention Overview

-	Error blocking

	-     error: missing/incorrect actions
	-     direct intervention to block errors
	      => fault injections prevented

	-     rely on technology/tools/etc.

-	Error source removal

	-     root cause analysis
	      => identify error sources

	-     removal through education/training/etc.

-	Systematic defect prevention via process improvement.

-	Details: Chapter 13.


# Formal Method Overview

-	Motivation

	-	fault present:

		-     revealed through testing/inspection/etc.

	-	fault absent: formally verify.

		(formal methods => fault absent)

-	Basic ideas

	-	behavior formally specified:

		-	 pre/post conditions, or
		-	 as mathematical functions.

	-	verify "correctness":

		-	 intermediate states/steps,
		-	 axioms and compositional rules.

	-	Approaches: axiomatic/functional/etc.

-	Details: Chapter 15.


# Inspection Overview

-	Artifacts (code/design/test-cases/etc.) from req./design/coding/testing/etc. phases.

-	Informal reviews:

	-	 self conducted reviews.
	-	 independent reviews.
	-	 orthogonality of views desirable.

-	Formal inspections:

	-      Fagan inspection and variations.
	-      process and structure.
	-      individual vs. group inspections.
	-      what/how to check: techniques.

-	Details: Chapter 14.


# Testing Overview

-	Product/Process characteristics:

	-	object: product type, language, etc.
	-	scale/order:
		unit, component, system, ...

	-	who: self, independent, 3rd party

-	What to check:

	-    	verification vs. validation
	-	external specifications (black-box)
	-	internal implementation (white/clear-box)

-	Criteria: when to stop?

	-	coverage of specs/structures.
	-	reliability => usage-based testing

-	Much, much more in Part II.


# Fault Tolerance Overview

-	Motivation

	-	fault present but removal infeasible/impractical

	-	fault tolerance => contain defects

-	FT techniques: break fault-failure link

	-  	recovery: rollback and redo
	-	NVP: N-version programming
		fault blocked/out-voted

-	Details: Chapter 16.


# Safety Assurance Overview

-	Extending FT idea for safety:

	-	fault tolerance to failure \tolerance"

-	Safety related concepts:

	-      	safety: accident free
	-	accident: failure w/ severe consequences
	-	hazard: precondition to accident

-	Safety assurance:

	-      hazard analysis
	-      hazard elimination/reduction/control
	-      damage control





# QA in Context

-       Defect Handling

-       QA in Software Processes

-       V&V Perspective

-       QA: Defect View vs V&V View


# QA in Context

-       QA and the overall development context

	-  defect handling/resolution
	-  activities in process
	-  alternative perspectives:

verification/validation (V&V) view

-       Defect handling/resolution

	-      status and tracking
	-      causal (root-cause) analysis
	-      resolution: defect removal/etc.
	-      improvement: break causal chain

# Defect Measurement and Analysis

-       Defect measurement:

	-      parallel to defect handling
	-      where injected/found?
	-      type/severity/impact?
	-      more detailed classification possible?
	-      consistent interpretation
	-      timely defect reporting

-       Defect analyses/quality models

	-      as followup to defect handling.
	-      data and historical baselines
	-      goal: assessment/prediction/improvement
	-      causal/risk/reliability/etc. analyses

-       Details in Part IV.


# QA in Software Processes

-       Mega-process:

	initiation, development, maintenance, termination.

-       Development process components:

	requirement, specification, design, coding, testing, release.

-       Process variations:

	-	waterfall development process
	-	iterative development process
	-	spiral development process
	-	lightweight/agile development processes and XP (extreme programming)
	-	maintenance process too
	-	mixed/synthesized/customized processes

-       QA important in all processes


# QA in Waterfall Process

![image](https://github.com/rplulbi/SQA/assets/15622730/02300adf-67b8-4931-b6dc-61d0193d92d1)


-       QA throughout process (Fig 4.1 p.45)

	-  defect prevention in early phases
	-  focused defect removal in testing phase
	-  defect containment in late phases
	-  phase transitions: inspection/review/etc.


# QA in Software Processes

-       Process variations (not waterfall) and QA:

	-	iterative: QA in iterations/increments
	-	spiral: QA and risk management
	-	XP: test-driven development
	-	mixed/synthesized: case specific
	-	more evenly distributed QA activities

-       QA in maintenance processes:

	-     	focus on defect handling;
	-	some defect containment activities for critical or highly-dependable systems;
	-	data for future QA activities

-       QA scattered throughout all processes


# V&V

-       Core QA activities grouped into V&V.

-       Validation: w.r.t. requirement (what?)

	-	appropriate/fit-for-use/\right thing"?
	-	scenario and usage inspection/testing;
	-	system/integration/acceptance testing;
	-	beta testing and operational support.

-       Verification: w.r.t. specification/design (how?)

	-	correct/\doing things right"?
	-	design as specification for components;
	-	structural and functional testing;
	-	inspections and formal verification.


# V&V in Software Process

![image](https://github.com/rplulbi/SQA/assets/15622730/9d295558-8120-4ba3-9b24-bd3987319ba9)

-       V&V in V-model above (Fig 4.2 p.49):

	-   V-model as bent-over waterfall
	-   left-arm: implementation (& V&V)
	-   right-arm: testing (& V&V)
	-   user@top vs. developer@bottom


# V&V vs DC View

-       Two views of QA:

	-   V&V view
	-   DC (defect-centered) view in this book
	-   Interconnected: mapping possible?

-       Mapping between V&V and DC view:

	-	V&V after commitment
		(defect injected already)
		=> defect removal & containment focus

	-	Verification: more internal focus
	-	Validation: more external focus
	-	In V-model: closer to user (near top) or developer (near bottom)?


# DC-V&V Mapping (Table 4.1, p.51)

![image](https://github.com/rplulbi/SQA/assets/15622730/3d6605ba-1979-474e-ae96-dcf602a7b75c)

