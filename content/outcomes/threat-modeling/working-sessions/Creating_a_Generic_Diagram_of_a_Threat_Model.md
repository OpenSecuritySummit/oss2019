---
title        :  Creating a Generic Diagram of a Threat Model 
type         : outcome
track        : Threat Model
video        :                    #url i.e. youtube, vimeo, etc
slides       :                    #url i.e. slideshare
images       :
session_type :                    # working-session, user-session, product-session            
technology   :
categories   :                    # GDPR, Juice Shop, etc.
status       : done              # draft, review-content, done
description  :
---

## Summary
Preparation session

A model of threat modeling

## Outcome
- Publish working draft
- (DSL session: what should it be usable for)
- Make model more cohesive
- Extended and/or peer-review on slack
- Extended by academia (?)

## Notes

Are 4 questions sufficient?

Question|Description 
--------|------------
Q1: System description|Model or Text? 
-|DSL would require some structure (e.g. (P)->(EE) )
-|Model - Diagram - View - Viewpoint
-|ISO 42010 (summary: http://www.iso-architecture.org/ieee-1471/cm/ - see notes below)
Q2: What can go wrong?|Risk vs. Threat?
-|  - Synopsis
-|  - OWASP risk rating
-| Firesmith - specifying reusable security requirements: http://www.jot.fm/issues/issue_2004_01/column6/
-|Use of kill chain
-|Meta language (to describe graphs, etc.)
Q3. Mitigation|Focus on mitigations
-|At least mention 4 different steps/options
Q4. validation|Checklist
-|Formal model
-|Context conditions

#### Summary of ISO 42010:
 - Model kind: conventions for a type of modelling. Examples of model kinds include data flow diagrams, class diagrams, Petri nets, balance sheets, organization charts and state transition models.
 - Architecture viewpoint:
Work product establishing the conventions for the construction, interpretation and use of architecture views to frame specific system concerns
 - Architecture view:
Work product expressing the architecture of a system from the perspective of specific system concerns
 - Architecture description AD:
Work product used to express an architecture

### Diagram

<img src="https://user-images.githubusercontent.com/22427294/58893966-0de31a80-86e9-11e9-90c5-debda7526773.png" width="75%">




