---
title        : OWASP SAMM Measurements
track        : Pre-Summit Working Session
video        : none
slides       : none
images       : none
session_type : working-session         
categories   : OWASP SAMM
status       : draft              

---

## Description of session

description  : The purpose of this session was to discuss measurement model aspects SAMM v2.0

## Notes from the working session (DRAFT)


The following are notes from the session - at this stage nothing was decided, rather a set of requirements were gathered to help aid and direct future conversations/ work in this space.

topics discussed:

should we measure "ownership" for the activities, practices? (RACI ?)

how about applicability (not all practices / activities are applicable)
model aims to be agnostic of process, technology or type of organisation

benchmarking, comparing aspects of the measurement.
ahead or behind "the pack"
objectices versus actual state



we considered qualitative indicators for STA1 during the call:
* the use of different tools
* the type of tools and if they are "fit for purpose"
* tools support regression testing
* false positive/negative rate of the tools
* are the vulnerabilities that are tested for regularly updated
* is the tooling outcome standardised (e.g. CVE numbers)

Other remarks or questions on the Security Testing practice:
Is bug bounties part of security testing?
Can known vulnerabilities be replicated (and are tests created for this)?


the questions to score the maturity should be optimised to discover the maturity with a minimum number of questions
e.g. what are the 5 most important questions to measure the maturity? Requiring less effort to measure.
Or what 50 questions do "matter" when measuring SAMM 
in a subsequent stage questions that are implementation or technology specific can be considered
(to be included as part of the guidance sections)
Also add (links to the) evidence whenever questions are answered.

## suggested followup actions:
* consider and build a conversion tool to upgrade V1.5 to V2.0 scores
* investigate samm scoring in Jupyter, Jira, Slackbot besides the Excel toolbox
* consider a graph database to collect scores and supporting facts and data points 
* Dinis recommends to gather public data through crowdsourcing questions and data points
The current model is "good enough" to start with a first set of questions
Community and real world feedback will then influence the model in a data supported manner.
adding questions to the security practices will trigger feedback and possibly refactoring of these practices.
* During the summit: gather questions during lunch from the summit participants (with direct feedback)


- last summit notes:  
https://github.com/OWASP/samm/edit/master/Supporting%20Resources/v2.0/summit-201810-Minneapolis/assessment-session.md
- tool from Dinis:
https://github.com/OWASP/Maturity-Models


