---
title        : Threat Modelling Data Schema
track        : Pre-Summit Working Session
video        : none
slides       : none
images       : none
session_type : working-session         
technology   : Data schema
categories   : Threat Modelling
status       : draft              

---

## Description of session

description  : The purpose of this session was to discuss requirements around a data schema for threat modelling to enable and/or support repeatable and automated threat modelling.

## Outcomes/Deliverables 

The conversation started with a walkthrough of the way Photobox are using vulnerability and risk data within JIRA to create graphs. 
This was done to show the potential of being able to harness usable threat data within a database to automatically create visual represenations of the threat landscape for an IT asset.
Link to slides on Photobox use of graphs (not used in the session but provides useful context): https://www.slideshare.net/DinisCruz/creating-a-graph-based-security-organisation-apr-2019-owasp-london-chapter-meeting


The following are notes from the session - at this stage nothing was decided, rather a set of requirements were gathered to help aid and direct future conversations/ work in this space.

# Non-Technical Requirements

- Tightly integrated with MITRE's ATT&CK, so everyone is "talking the same language"
- Embrace DevSecOps methodology; this idea needs to be implemented and then modified appropriately, rather than expecting to get the solution the 1st time
- Must support TM at all stages of the SDLC
- Must be able to show the impact of a proposed update to a service (branch TM's)


# Technical Requirements

- Support versioning
- Automaticaly generate threats based on certain captured characteristics (e.g. internet facing, technology XYZ)
- Automatically generate graphs/ diagrams based on added content and data links
- Be able to model dataflow, process, external entity, data storage, trust boundaries
- Automaticly generate STRIDE tables for trust boundaries 
- Identify sensitive/confidential data
- Support custom data sensitivity/ confidentiality levels
- Identify PII data on the model







## Synopsis and Takeaways (recommend)
- Wider session requested on data schemas / automated threat modelling and tech stacks - working session to be added to Summit schedule. 


## Identified Questions
- Where automation is utilised, how do we ensure we don't remove engineers abilities to learn from the threat modelling process, contribute and collaborate with security teams.
- By removing the manual process are we potentially missing threats captured from engineers contributions?
- How much data should be captured in a threat model? When is there too much data?
- What data shouldn't be in a threat model (assuming it's captured elswhere?)
- Should CVE's be present?
- Should SAST/ pen test output be present?

## Follow up
- Presentation from Toreon team requested on the work they're doing in this space (none of the project team were able to make the session)


## References 
- https://www.slideshare.net/DinisCruz/creating-a-graph-based-security-organisation-apr-2019-owasp-london-chapter-meeting
- Sample draft data schema from Tash Norris: https://twitter.com/TashJNorris/status/1120057714971947008 

