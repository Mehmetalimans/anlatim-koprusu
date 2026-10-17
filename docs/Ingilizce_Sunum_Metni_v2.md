# Anlatım Köprüsü - English slide copy

**Prototype review draft, 17 October 2026.** v2: Yerel uygulama ve 68 çevrimdışı test doğrulandı. Gerçek model ve karşılaştırma bekliyor. Bu metin sunumun içerik ve konuşmacı notlarını tutar.

## 1. Anlatım Köprüsü

Academic language, explained in context

Group 14

Prototype review draft, 17 October 2026

## 2. A phrase can block understanding

Academic expression: “The value of the best alternative forgone.”

If Deniz chooses studying and would otherwise choose the concert, the concert is the alternative he gives up.

The student selects the phrase. The source stays visible.

Speaker note: This is a team-written learning example, not a screenshot or live AI output. Source: OpenStax Principles of Economics 3e, section 2.1.

## 3. The learning cycle

1. Choose a source and a phrase.
2. Read the explanation and source references.
3. Apply the idea in a new question.
4. Explain the answer and review feedback.

Feedback addresses the selected answer and the written reason.

Speaker note: Implemented in the local prototype and checked with controlled responses. Live model quality is pending. The option outcome is computed from the generated key in code; keys need human review.

## 4. One workflow across three subjects

| Subject | Focus | Meaning to preserve |
| --- | --- | --- |
| Physics 2 | Potential and potential energy | Units and charge signs |
| ECON 100 | Opportunity cost | The best forgone alternative |
| Basic Python | for loops and range | Indentation and stop boundaries |

Speaker note: All three inputs load in the app. Live-model evaluations are pending. Sources: OpenStax University Physics Volume 2, section 7.2; OpenStax Principles of Economics 3e, section 2.1; Python official tutorial, range.

## 5. Prompt design and checks

Two model tasks:

- Generate the explanation and question.
- Respond to the student's written reason.

Checks in the prototype:

- Preserve meaning and valid references.
- Review question keys and feedback.
- Handle insufficient context and API errors.

Compare prompt versions using the same input texts.

Speaker note: The comparison has not been run. Schema validation checks structure and does not establish semantic correctness.

## 6. Evidence, limits and SDG 4

Verified offline:

- Three courses loaded in the app.
- 68 automated tests passed.

Pending:

- Live API and model quality.
- Prompt comparison and final video.

SDG 4: access to understandable learning support.

Learning gains have not been measured.

Speaker note: Offline tests use controlled responses with network blocked. They do not establish live model quality. Development feedback is canned and is not rationale-aware AI evaluation. Target 4.3 includes equal access to quality tertiary education. The project's intended contribution is learning support, not a measured change in education access.

## Sources

- https://github.com/Mehmetalimans/anlatim-koprusu
- https://sdgs.un.org/goals/goal4
- https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference
- https://openstax.org/books/principles-economics-3e/pages/2-1-how-individuals-make-choices-based-on-their-budget-constraint
- https://docs.python.org/3/tutorial/controlflow.html#the-range-function
