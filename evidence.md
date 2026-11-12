# Nexus lab evidence

## Contributors and participation
Names; who typed, traced behavior, designed or checked tests. Ad hoc groups are fine.

## Baseline
Pinned upstream: 75a8d145aa5bc0c92725197c0e4e9883491c542f.
Interpreter/version, command, actual output. Expected starter: four passes, four failures.

## Our design decision
Audit owner and interface; ordering; one credible alternative; accepted benefit/cost.


owner: auditor class (contains list of audits, has a record function for adding an audit record to the list)
call that records audit history: 
what is the audit recorded relative to the public event/publication:
what cost is introduced:


Thursdays:
because of our design tuesday of having a list that was accessed via a add record and a get records call, all we had to implement for an audit file was upon intantiation of the auditor class, we read the file into that list, and then as we append records, we just append the list and the file



## Actual changes
Changed files/functions. What is implemented versus still proposed?
Explain the sanctioned original notification-test expectation change.

## Our added behavior check
Conditions, action, expected observable result and reason for choosing it.

## Final execution evidence
Command and actual output. Separate the lab runner from the original pytest suite.
If a command was not run, say so. Preserve remaining failures and their meaning.

## Limitations and next step
What do the results not establish? What would you check next?

## Individual PR starting points
Each person separately: initial claim, consequential challenge, current disposition.
Copy the shared code/evidence before leaving. No submission is due at class end.
