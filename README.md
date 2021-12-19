# Multi Half-Life Calculator

## Description
Though there are many half-life calculators on the web,
there are few that support multiple / repeat doses.
This project attempts to be one that does.
This is intended primarily for a pharmacological context,
rather than for a radiological context.

## Vocabulary
* Substance (_noun_)
 - A specific chemical (including medicines, drugs).
* Dose (_noun_)
 - The QUANTITY of substance intake during a single time
   - (e.g. an administration of 100mg of medicine).
* Dose (_verb_) [dosing, dosed, will dose]
 - The ACT of substance intake.
* Dosage (_noun_)
 - The ACT of substance intake.

"His dosing frequency is two dosages each day, and each of said dosages consists of a dose of 100mg."

## Instructions
Enter the following information:
* Substance's half-life (e.g. "hours=18")
* Dose (e.g. 200. Assumes that this is consistent)
* Frequency of dosing (e.g. "days=1", AKA time between each administration. Assumes this is consistent)
* End date

## Limitations
* This is a personal project and not medical advice.
* This does not account for the situation that the substance is also produced endogenously. [1]
* This does not account for non-instant absorption rates. I.e. this assumes tmax=0s, which in reality is always incorrect. [1]
* This assumes that the dosages are consistent. [1]

[1] = This may be fixed / improved in a future version.

## Possible improvements
* Prompts user for inputs (e.g. half-life, dose).
* Fixing the fixable limitations.
* Output is a graph.
* Multiple end options: a specific end date, or a max quantity of dosages, or a max dose (e.g. max quantity of substance).
* Support for inconsistent dose (e.g. 100mg, and then 200mg).
* Support for inconsistent dosage timing (e.g. a dose every. Wednesday and Thursday, or even more random).
* User can customize the units (e.g. mg, g, mL, L, mSv, Sv, Gy).
* Make this into a web-app.
* Supports multiple different substances in one graph.
