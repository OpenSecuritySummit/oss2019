---
title        : Mobile Basic Security Testing and Reverse Engineering (Tue Evening)
type         : working-session    # working-session, user-session
track        : OWASP MSTG
technology   : Mobile, iOS, Android
categories   : MSTG                   # GDPR, Juice Shop, etc.
featured     :                # review with summit team "yes"
when_day     : Tue
when_time    : Eve-1,Eve-2
room_layout  :                    #
room_id      : villa-3
session_slack:
status       : review-content              # draft, review-content, done
organizers   : 
  - Carlos Holguera
description  : Work on the Mobile Basic Security Testing and Reverse Engineering topics with focus on restructuring the contents of the MSTG
participants:
  - Jeroen Beckers
  - Sven Schleier
  - Jeroen Willemsen
---

Welcome to the ultimate OWASP Mobile Security Testing Guide content reshuffle session!

## Why

If you're familiar with mobile security testing you'll probably know that the way we perform the testing on the different platforms is completely different but at the end, what we want to achieve is the same. We want to get this reflected in the guide. We will be working on topics **from basic to advanced Mobile App Security Testing, Reverse Engineering and Tampering** on Android and iOS.

As a result, the current content will be restructured, which will help

- achieving a more organized testing approach and methodology.
- detecting potential missing tools or techniques.
- fixing missing links across chapters.

Android and iOS chapter will *mirror* each other, so the next time someone (e.g. a beginner) wants to get started on these topics it will be very clear what has to be done and how. If you're already an expert on e.g. Android, this will help you quickly identify the things you need when starting testing on iOS, e.g. "Accessing the Device Shell".

## What

Join us in a 2-day sprint to restructure the basic-testing and reverse-engineering chapters in a way that they are easily mappable. We want to be able to restructure the MSTG and connect it to the MASVS in a better way during the first 2 days in order to make the chapters more accessible.

This session focus on the following topics (and their corresponding chapters from the [MSTG](https://github.com/OWASP/owasp-mstg)):

- Android and iOS Basic Security Testing ([0x5b](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05b-Basic-Security_Testing.md)/[0x6b](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06b-Basic-Security-Testing.md))
- Android and iOS Reverse Engineering and Tampering ([0x5c](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05c-Reverse-Engineering-and-Tampering.md)/[0x6c](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06c-Reverse-Engineering-and-Tampering.md))

After the first restructuring and updated outline, you'll have the chance to **get your hands dirty** and craft examples and new content for the MSTG to add next to existing tooling. For the new examples we will be introducing new tools like r2frida. **Did you know you can reverse engineer an app straight from the process memory?** That means, e.g. for iOS that you may skip the decryption and extraction of the binary.

The tickets for this working session will cover these topics and contribute to the restructuring of the MSTG [as described in this issue](https://github.com/OWASP/owasp-mstg/issues/970). This should simplify the chapters, improve their readability and make the project a lot easier to maintain!

## Who

The target audience for this Working Session is:

- iOS developers
- Android developers
- Penetration Testers
- Security engineers

From experts to beginners. Anybody who is passionate about app mobile security, haves fun hacking, securing and/or developing mobile apps and loves to continuously learn and enjoys sharing knowledge.

## What do you need to bring with you?

Minimum required: a laptop :)

Depending on the tasks/challenges you choose:

- General rewriting tasks do not require any devices, however if you want to add new cases, then:
  - For iOS: an iOS device (preferably jailbroken). A MacBook is recommended but not mandatory.
  - For Android: an Android device is highly recommended (preferably rooted). However for many tasks you can use the emulator.

The MSTG is hosted in GitHub and can easily be edited by anyone, just a Github account is needed and knowledge on how to create a pull request.

## Outcomes

A beautifully restructured MSTG.

## References

- ["Basic Security Testing / Reverse Engineering and Tampering" Chapters Restructuring Issue](https://github.com/OWASP/owasp-mstg/issues/970)
- [Android Basic Security Testing](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05b-Basic-Security_Testing.md)
- [Android Reverse Engineering and Tampering](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05c-Reverse-Engineering-and-Tampering.md)
- [iOS Basic Security Testing](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06b-Basic-Security-Testing.md)
- [iOS Reverse Engineering and Tampering](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06c-Reverse-Engineering-and-Tampering.md)
