---
title        : Dealing with DevSecOps Findings
type         : working-session
track        : DevSecOps
topics       : ["SDL"]
technology   : Dependency Check, FindSecBugs, ZAP, Jenkins, Defect Dojo, Selenium, Jira, Juice Shop
categories   :                      
featured     : yes                  
when_day     : Wed
when_time    : PM-1,PM-2
room_layout  :
room_id      : room-5
session_slack: #w-devsecops-findings 
status       : review-content              # draft, review-content, done
organizers   : 
 - Claudio Camerino
 - Francisco Novo
 - Rafael Jimenez
participants : 
description  : How to deal with the security findings in an appsec pipeline and drive continuous improvement of the testing policies

---

Security testing is vital to validate the correct implementation of controls and that security requirements. To scale securty testing to often hundreds of different software products, many organisations now implement automated tools to scale security testing practices. In this hands-on working session we'll learn how to build a working DevSecOps POC and, more importantly, how to deal with the myriad of security findings it generates.

## Why

Thanks to the proliferation of automated security scanning tools we are generating a phenomenal amount of security findings. As part of  this session we tackle the following goals.

1. Increase Visibility - Can't secure what you don't see. Why is important to test early in the SDL and map tests to QA business flows.
2. Define Accountability - Creating a feedback loop with your Devs. Why is important to flag findings to their respective owners and incorporate Devs feedback into testing policies.
3. Improve Noise Removal - Accuracy drives credibility. Devs are more likely to triage and action reputable findings, starting with tighter scan policies.
4. Achieve Scalability - Running tools and managing processes manually is not an option when dealing with hundreds of products. How to scale generation, collection and triaging of security findings.

## What

- Explore the automated testing workflow, participants will be encouraged to take part and share their experience.
- What selection of tools and test types should be used to generate security findings as part of a DevSecOps program.
- Reccommended security testing approaches for:
-- Frontend vs backend applications
-- Static vs runtime
- Why is important to have a single source of truth for multiple testing tools
- AppSec testing integration with QA - user stories vs abuse cases and how to leverage QA processes to drive ZAP.
- Integration with Jira - how to raise and populate SEC type tickets and track their lifecycle.
- Continuous improvement - how to tune security policies as result of the triage process

## Outcomes
- Build and run a working DevSecOps POC lab from open source tools
- Define ruleset for programmatic removal of noise (e.g. duplicates, fixes in progress and easy to spot false positives)
- Learn how to adapt/hack OSS tools like ZAP and Defect Dojo for enterprise level automation.
- Define roles and responsibilities for an appsec pipeline based on common industry roles (QA, Del Svcs, Engineering etc.)
- Create CD scripts to automate generation, collection and allocation of findings.
- Generation of:
-- ZAP scan policies, contexts and ZEST scripts
-- SAST SonarQube quality profiles
-- Dependency Check Configuration
-- Defect Dojo/Jira integration Scripts
-- Jenkins groovy scripts to tie it all together ..


## Who

The target audience for this Working Session is:

 - Developers
 - Security professionals
 - DevOps / DevSecOps
 - Security champions
 - AppSec leaders

## Working materials

Here are the current materials for this session:

- [The Security Development Lifecycle](https://www.owasp.org/images/7/78/OWASP_AppSec_Research_2010_Keynote_2_by_Lipner.pdf)
- [SDL in Practice](https://www.owasp.org/images/4/45/SDL_in_practice.pdf)
- [Defect Dojo](https://github.com/DefectDojo/django-DefectDojo)
- [OWASP ZAP](https://github.com/zaproxy/zaproxy)
- [Dependency Check](https://github.com/jeremylong/DependencyCheck)
- [Selenium](https://www.seleniumhq.org/projects/webdriver)

## Previous Summit Working Session
