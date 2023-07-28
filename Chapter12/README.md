# Chapter 12

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

![image](https://github.com/rplulbi/SQA/assets/15622730/5147a6c5-7814-4e5e-867c-6f0307fcb82b)

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

![image](https://github.com/rplulbi/SQA/assets/15622730/8ba1dd42-a2fa-48b3-a6ae-318303804dc6)


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

![image](https://github.com/rplulbi/SQA/assets/15622730/7365d007-4303-411d-87d2-ed4daa421ef3)


-       Effort profile above (Fig 5.3, p.63)

	-      planning/QA/analysis of total effort
	-      general shape/pattern only

	       (actually data would not be as smooth)

	-      in other processes:

	       - similar but more evenly distributed


# Testing Overview

-       Testing: Concepts & Process

-       Testing Related Questions

-       Major Testing Techniques

# Testing and QA Alternatives

-   Defect and QA:

	- Defect: error/fault/failure.
    - Defect prevention/removal/containment.
    - Map to major QA activities

-       Defect prevention:

# Error blocking and error source removal.

-       Defect removal:

	-	Testing  
	-	Inspection, etc.

-       Defect containment: Fault tolerance and failure containment (safety assurance).

# QA and Testing

-       Testing as part of QA:

	- Activities focus on testing phase
	- QA/testing in waterfall and V-models

		(Fig 4.1, p.45 and Fig 4.2, p.49)

	- One of the most important part of QA

		- defect removal: Fig 3.1 (p.30)

-       Testing: Key questions:

	- Why: quality demonstration vs. defect detection and removal
	- How: techniques/activities/process/etc.
	- View: functional/external/black-box vs. structural/internal/white-box
	- Exit: coverage vs. usage-based

# Testing: Why?

-       Original purpose: demonstration of proper behavior or quality demonstration.

		~ "testing" in traditional settings.
	-	 evidence of quality or proper behavior.

-       New purpose: defect detection & removal:

	- mostly defect-free software manufacturing vs. traditional manufacturing.

	- flexibility of software (ease of change; sometimes, curse of change/flexibility)

	- failure observation => fault removal.

		 (defect detection => defect fixing)

	- eclipsing original purpose

# Testing: How

-       How? Run-observe-followup

		(particularly in case of failure observations)

-       Refinement

		=> generic process below (Fig 6.1, p.69)

![image](https://github.com/rplulbi/SQA/assets/15622730/58c48ebf-c9ac-4c67-ae6e-b16ce0bbdccb)

-       Generic testing process as instantiation of SQE process in Fig 5.1, p.54.

# Testing: Activities & Generic Process

-       Major testing activities:

	- test planning and preparation
	- execution (testing)
	- analysis and followup

-       Link above activities ) generic process:

	- planning-execution-analysis-feedback.
	- entry criteria: typically external.
	- exit criteria: internal and external.
	- some (small) process variations

		- but we focus on strategies/techniques.

# Testing: Planning and Preparation

-       Test planning:

	- goal setting based on customers’ quality perspectives and expectations.
	- overall strategy based on the above and product/environmental characteristics.

-       Test preparation:

	- preparing test cases/suites:

		- typically based on formal models.

	- preparing test procedure.

-       More details in Chapter 7.

# Testing: Execution

-       General steps in test execution

	- allocating test time (& resources)
	- invoking test
	- identifying system failures (& gathering info. for followup actions)

-       Key to execution: handling both normal vs. abnormal cases

-       Activities closely related to execution:

	- failure identification:

		test oracle problem

	- data capturing and other measurement

-       More details in Chapter 7.

# Testing: Analysis and Followup

-       Analysis of testing results:

	- result checking (as part of execution)
	- further result analyses

		- defect/reliability/etc. analyses.

	- other analyses: defect ~ other metrics.

-       Followup activities:

	- feedback based analysis results.
	- immediate: defect removal (& re-test)
	- other followup (longer term):

		- decision making (exit testing, etc.)
		- test process improvement, etc.

-       More details in Chapter 7 (for activities) and Part IV (for mechanisms/models/etc.).

# Testing: How?

-       How to test?

		-	refine into three sets of questions

	- basic questions
	- testing technique questions
	- activity/management questions

-       Basic questions addressed in Ch.6:

	- What artifacts are tested?
	- What to test?

		- from which view?
		- related: type of faults found?

	- When to stop testing?

# Testing Technique Questions

-       Testing technique questions:

	- specific technique used?
	- systematic models used?

		- related model questions (below)

	- adapting technique from other domains?
	- integration for efficiency/effectiveness"?

-       Testing model questions:

	- underlying structure of the model?

		- main types: list vs. FSM?

	- how are these models used?
	- model extension?

-       Major techniques: Chapters 8-11.

# Test Activity/Management Questions

-       Addressed already: Generic process and relation to QA and software processes.

-       Other activity/management questions:

	- Who performs which specific activities?
	- When can specific activities be performed?
	- Test automation? What about tools?
	- Artifacts used for test management?
	- General environment for testing?
	- Product type/segment?

-       Most questions answered in Chapter 7.

	Integration issues addressed in Chapter 12.

# Functional vs. Structural Testing

-       Key distinction: Perspective on what need to be checked/tested.

-       Functional testing:

	- tests external functions.

		- as described by external specifications

	- black-box in nature;

		- functional mapping: input ) output
		- without involving internal knowledge

-       Structural testing:

	- tests internal implementations.

		- components and structures.

	- white-box in nature;

		- "white" here = seeing through

			=> internal elements visible.

	- really clear/glass/transparent box.

# Black-Box vs. White-Box View

-       Object abstraction/representation:

	- high-level: whole system ~ black-box.
	- low-level: individual statements, data, and other elements ~ white-box.

	- middle-levels of abstraction:

		- function/subroutine/procedure, module, subsystem, etc.

		- method, class, super-class, etc.

-       Gray-box (mixed black-box/white-box) testing:

	- many of the middle levels of testing.
	- example: procedures in modules

		- procedures individually as black box,
		- procedure interconnection ~ white-box at module level.

# White-box Testing

-       Program component/structure knowledge

	(or implementation details)

	- statement/component checklist
	- path (control flow) testing
	- data (flow) dependency testing

-       Applicability

	- test in the small/early
	- dual role of programmers/testers
	- can also model specifications

-       Criterion for stopping

	- mostly coverage goals.
	- occasionally quality/reliability goals.

# Black-box Testing

-       Input/output behavior

	- specification checklist.
	- testing expected/specified behavior

		- finite-state machines (FSMs)

	-	 white-box technique on specification
		- functional execution path testing.

-       Applicability

	- late in testing: system testing etc.
	- suitable for IV&V
	- compatible with OO/Reuse paradigm

-       Criteria: when to stop

	- traditional: functional coverage
	- usage-based: reliability target

# When to Stop Testing

-       Resource-based criteria:

	- Berhenti ketika Anda kehabisan waktu.
	- Berhenti ketika Anda kehabisan uang.
	- Tidak bertanggung jawab masalah kualitas/lainnya.

-       Quality-based criteria:

	- Berhenti ketika tujuan kualitas tercapai.
	- Ukuran kualitas langsung: keandalan (Reliability)

		- menyerupai penggunaan pelanggan yang sebenarnya
		
	- Ukuran kualitas tidak langsung: coverage.
	- Pengganti lainnya: penyelesaian aktivitas.
	- Di atas dalam penurunan keinginan.

# Usage-Based Testing and OP

-       Usage-based statistical testing:

	- penggunaan aktual dan skenario/informasi
	- ditangkap dalam profil operasional (OP)
	- disimulasikan dalam lingkungan pengujian

		(terlalu banyak => pengambilan sampel acak)

-       Applicability

	- tahap akhir pengujian.
	- particularly system/acceptance testing.
	- pakai s/w reliability engineering.

-       Termination criteria: reliability goals

# Coverage-Based Testing

-       Coverage-based testing:

	- pengujian sistematis berdasarkan model dan teknik formal (BBT/WBT).
	- ukuran coverage yang ditentukan untuk model
	- testing managed by coverage goals

-       Applicability

	- semua tahapan pengujian.
	- khususnya pengujian unit dan komponen.
	- fase selanjutnya pada tingkat abstraksi tinggi.

-       Termination criteria: coverage goals

# Steps in Systematic Testing

-       Instantiation of Fig 6.1 (p.69), but,

	- dengan strategi/tujuan yang diformalkan,
	- berdasarkan model dan teknik formal,
	- dikelola oleh kriteria terminasi.

-       Steps in model construction and usage:

	- Tentukan model, biasanya direpresentasikan sebagai grafik dan relasi.
	- "Periksa" elemen individual:
	- "Test": dapatkan (sensitisasi) kasus uji dan kemudian jalankan.

. Result checking and followup.

-       Specifics on model construction and usage in individual testing techniq
