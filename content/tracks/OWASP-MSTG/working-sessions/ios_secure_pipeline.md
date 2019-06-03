---
title        : Creating an iOS build pipeline with security checks 
type         : working-session    # working-session, user-session
track        : OWASP MSTG
technology   : Mobile, iOS
categories   : MSTG                   # GDPR, Juice Shop, etc.
featured     : yes                # review with summit team "yes"
when_day     : Wed
when_time    : AM-1
room_layout  :                    #
room_id      : room-5
session_slack:
status       : review-content              # draft, review-content, done
organizers   : Sven Schleier
description  : Brainstorming for a iOS pipeline with security checks
---

This session is about creating a blueprint for an iOS build pipeline that includes security checks/tools.

## Why

Security tools for iOS are usually very limited at the moment or have no wide coverage. Let's identify the tools that work at the moment and bring value for an iOS pipeline.

## What

We want to make a summary of best practices and tools that should be part of an iOS pipeline and want to answer the following questions:

- Which approach, scripts or (Open Source) tools can be used for an iOS pipeline:
  - To detect secrets
  - To do secret management
  - To scan source code (Objective-C and Swift)
  - To test if SSL Pinning is activated
  - To test if Root detection is activated
  - To test the configuration of ATS
  - To check 3rd party libraries (CocoaPods and Carthage) and their licene
- How to maintain the certificates for signing an app?

The outcome of this session will be captures in the following public Github Repo: <https://github.com/sushi2k/iOS_pipeline>

## Who

The target audience for this Working Session is:

- iOS developers
- Penetration Testers
- DevOps engineers
- Security engineers

From experts to beginners. Anybody who is passionate about iOS mobile security, haves fun hacking, securing and/or developing mobile apps and loves to continuously learn and enjoys sharing knowledge.

## What do you need to bring with you?

Ideally a laptop (a MacBook is recommended, but not mandatory) to do research for tools, do PoC and contribute to the Github repo. Otherwise contributions can also be done verbally and the team will push to the repo.

The outcome is hosted in GitHub and can easily be edited by anyone, just a Github account is needed and knowledge on how to create a pull request.

## Outcomes

A summary of best pratices and tools on how to build an iOS pipeline.

## References

- TBD