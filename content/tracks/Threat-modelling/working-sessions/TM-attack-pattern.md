---
title        : Threat pattern libraries
type         : working-session
track        : Threat Model
locked       : false
technology   :
categories   :                      # GDPR, Juice Shop, etc.
featured     :                    # review with summit team "yes"
when_day     : Wed
when_time    : PM-2
room_layout  :                    #
room_id      : room-3
session_slack: 
status       : done              # draft, review-content, done
description  : Starting the threat model threat model library project 
organizers   :
    - Steven Wierckx
    - Steven van der Baan
participants:
    - Tash Norris
---

This session will be the start of a sub-project for threat modeling that will be lead by Steven and Steven that will create a database of attacks and mitigations that will be categorised in some kind of pattern.

##outcomes

This is the data format in which we are going to record the data:

Threat file
1	ID (generated)

2	Description
		As an attacker
		I want to ... <cause an impact>
		By ... <how does an attacker do this?>
		Or by ... <how does an attacker do this?>

		(optional multiple)
		As an attacker
		I want to ... <cause an impact>
		By ... <how does an attacker do this?>
		Or by ... <how does an attacker do this?>

3	References
		List

4	See also
		Mapping
			List of ...
			List of ...

5	Tags
		List (limited list of tags)

6	Origin
		Project & Project ID


Mitigation file
1	ID (generated)

2	Description
		As an defender
		I want to Prevent <threat?>
		By ... <how does an defender do this?>
		Or by ... <how does an defender do this?>

		(optional multiple, cover the mapping of threats)
		As an defender
		I want to Prevent <threat?>
		By ... <how does an defender do this?>
		Or by ... <how does an defender do this?>

3	References
		List

4	See also
		Mapping
			List of ...
			List of ...

5	Tags
		List (limited list of tags)

6	Origin
		Project & Project ID


Mappings
Threat -> mitigation (risidual risk)
Mitigation -> threat (is in the mitigation file under description)
Threat -> Threat
Mitigation -> mitigation
Mitigation -> threat (a mitigation can cause a new threat to appear) -> causes chains of mitigations to be implemented
Threat -> external reference (CAPEC, CVE, CWE)
Mitigation -> external reference?
Threat -> examples
Mitigation -> examples
Threat -> symptoms
Threat -> threat -> kill chain


Action points
- check pytm to use a better/more efficient format

Additional references that miht prove interesting:
https://www.owasp.org/index.php/OWASP_Proactive_Controls Technical migitation
https://www.owasp.org/index.php/OWASP_Java_HTML_Sanitizer_Project https://cwe.mitre.org/top25/mitigations.html 
https://cwe.mitre.org/top25/mitigations.html
