---
title        : OWASP SAMM Measurements
track        : Pre-Summit Working Session
video        : none
slides       : none
images       : none
session_type : working-session         
categories   : OWASP SAMM
status       : done              
type         : outcome
---

## Description of session

The purpose of this session was to discuss measurement model aspects SAMM v2.0

## Notes from the working session

The following are notes from the session - at this stage nothing was decided, rather a set of requirements were gathered to help aid and direct future conversations/ work in this space.

**Topics discussed**

- Should we measure "ownership" for the activities, practices? (RACI ?)

- How about applicability (not all practices / activities are applicable)
- Model aims to be agnostic of process, technology or type of organisation
- Benchmarking, comparing aspects of the measurement
- Ahead or behind "the pack"
- Objectives versus actual state


**We considered qualitative indicators for STA1 during the call**
- The use of different tools
- The type of tools and if they are "fit for purpose"
- Tools support regression testing
- False positive/negative rate of the tools
- Are the vulnerabilities that are tested for regularly updated
- Is the tooling outcome standardised (e.g. CVE numbers)

**Other remarks or questions on the Security Testing practice**
- Are bug bounties part of security testing?
- Can known vulnerabilities be replicated (and are tests created for this)?
- The questions to score the maturity should be optimised to discover the maturity with a minimum number of questions
e.g. what are the 5 most important questions to measure the maturity? Requiring less effort to measure.
- Or, what 50 questions do "matter" when measuring SAMM 
- At a subsequent stage questions that are implementation or technology specific can be considered
(to be included as part of the guidance sections)
- Also add (links to the) evidence whenever questions are answered.

## Suggested followup actions
- Consider and build a conversion tool to upgrade V1.5 to V2.0 scores
- Investigate SAMM scoring in Jupyter, Jira, Slackbot besides the Excel toolbox
- Consider a graph database to collect scores and supporting facts and data points 
- Dinis recommends to gather public data through crowdsourcing questions and data points
- The current model is "good enough" to start with a first set of questions
- Community and real world feedback will then influence the model in a data supported manner
- Adding questions to the security practices will trigger feedback and possibly refactoring of these practices.
- During the summit: gather questions during lunch from the summit participants (with direct feedback)

## Further resources
- 2018 Summit notes:  
https://github.com/OWASP/samm/edit/master/Supporting%20Resources/v2.0/summit-201810-Minneapolis/assessment-session.md
- tool from Dinis: https://github.com/OWASP/Maturity-Models


