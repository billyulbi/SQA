# Chapter 12

Software Quality Engineering
============================

	Testing, Quality Assurance, and Quantiable Improvement

Tian Siyuan <tiansiyuan@gmail.com>

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

![](../pics/4-1.png)

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

![](../pics/4-2.png)

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

![](../pics/4-3.png)


Software Quality Engineering
============================

	Testing, Quality Assurance, and Quantiable Improvement

Tian Siyuan <tiansiyuan@gmail.com>

# Quality Engineering

-       SQE: Software Quality Engineering

-       Key SQE Activities

-       SQE in Software Process


# QA to SQE

-       QA activities need additional support:

	-  Planning and goal setting
	-  Management:

	   -	when to stop?
	   -	adjustment and improvement, etc.
	   -	all based on assessments/predictions

-       Assessment of quality/reliability/etc.:

	-  Data collection needed
	-  Analysis and modeling
	-  Providing feedback for management

-       QA + above

	=> software quality engineering (SQE)


# SQE Process

![](../pics/5-1.png)

-       SQE process to link major SQE activities: Fig 5.1 (p.54)

	-   Pre-QA planning;
	-   QA: covered previously (Ch.3 & 4);
	-   Post-QA analysis and feedback
	    (maybe parallel instead of "post-")


# SQE and QIP

-       QIP (quality improvement paradigm):

	-   Step 1: understand baseline
	-   Step 2: change then assess impact
	-   Step 3: package for improvement

-       QIP support:

	-   overall support: experience factory
	-   measurement/analysis: GQM
	    (goal-question-metric paradigm)

-       SQE as expanding QA to include QIP ideas.


# Pre-QA Planning

-       Pre-QA planning:

	-      Quality goal
	-      Overall QA strategy:

	       -       QA activities to perform?
	       -       measurement/feedback planning

-       Setting quality goal(s):

	-	Identify quality views/attributes
	-	Select direct quality measurements
	-	Assess quality expectations vs. cost


# Setting Quality Goals

-       Identify quality views/attributes

	-	 customer/user expectations,
	-	 market condition,
	-	 product type, etc.

-       Select direct quality measurements

	-      direct: reliability
	-      defect-based measurement
	-      other measurements

-       Assess quality expectations vs. cost

	-      cost-of-quality/defect studies
	-      economic models: COCOMO etc


# Forming QA Strategy

-       QA activity planning

	-  evaluate individual QA alternatives

	   -	    strength/weakness/cost/applicability/etc.

	-  match against goals
	-  integration/cost considerations

-       Measurement/feedback planning:

	-  define measurements (defect & others)
	-  planning to collect data
	-  preliminary choices of models/analyses
	-  feedback & followup mechanisms, etc.


# Analysis and Feedback

-       Measurement:

	-	defect measurement as part of defect handling process

	-	other data and historical baselines

-       Analyses: quality/other models

	-	input: above data
	-	output/goal: feedback and followup
	-	focus on defect/risk/reliability analyses

-       Feedback and followup:

	-	 frequent feedback: assessments/predictions
	-	 possible improvement areas
	-	 project management and improvement

-       Details in Part IV.


# SQE in Software Processes

-       SQE activities are part of development activities:

	-   quality planning is part of product planning
	-   QA activities are part of development activities
	-   analysis/feedback is part of project management

-       Fitting SQE in software processes:

	-	different start/end time
	-	different sets of activities, sub-activities, and focuses

	-	in waterfall process: more staged

		(planning, execution, analysis/feedback)

	-	in other processes:

		more iterative or other variations


# SQE in Waterfall Process

![](../pics/5-2.png)

-       Fig 5.2 (p.61) above

	-   activity start/finish line
	-   different focus and effort (later)


# SQE Effort Profile

-       QE activity/effort distribution/dynamics:

	-  different focus in different phases
	-  different levels (qualitatively)
	-  different build-up/wind-down patterns
	-  impact of product release deadline

		(deadline-driven activities)

-       planning: front heavy

-       QA: activity mix

		(early vs. late; peak variability? deadline?)

-       analysis/feedback: tail heavy

		(often deadline-driven or decision-driven)


# SQE Effort in Waterfall Process

![](../pics/5-3.png)

-       Effort profile above (Fig 5.3, p.63)

	-      planning/QA/analysis of total effort
	-      general shape/pattern only

	       (actually data would not be as smooth)

	-      in other processes:

	       - similar but more evenly distributed
