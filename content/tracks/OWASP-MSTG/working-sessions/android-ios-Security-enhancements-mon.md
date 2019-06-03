---
title        : Android and iOS Security Enhancements and Crackme Apps (Mon)
type         : working-session    # working-session, user-session
track        : OWASP MSTG
technology   : Mobile, iOS, Android
categories   : MSTG                   # GDPR, Juice Shop, etc.
featured     : yes                # review with summit team "yes"
when_day     : Mon
when_time    : DS-2,PM-1,PM-2,PM-3
room_layout  :                    #
room_id      : room-5
session_slack:
status       : review-content              # draft, review-content, done
organizers   :
    - Sven Schleier
description  : Updating the content of the MSTG
participants:
    - Jeroen Willemsen
    - Jeroen Beckers
    - Carlos Holguera
---

Welcome to the OWASP Mobile Security Testing Guide Content pressure cook!

## Why

Staying up-to-date is key, especially regarding mobile security. We have the chance to do it all together in the same place! In this 5 day-continuous sprint, we want to make the MSTG greater than ever! To do this, there are streams that will require constant attention: the guide itself and the apps that we use for examples.

## What

### Get to share the latest Android and iOS security enhancements

The first stream is all about making the guide up to date with the latest security updates on iOS 12, Android 9 and 10:

iOS 12:

- UIWebViews are officially deprecated
- new AuthenticationServices and Network Frameworks
- New Password AutoFill Framework for iOS and web apps
- ...

Android 9/10:

- Scoped Storage: an isolated storage sandbox right on external storage device! The READ_ and WRITE_EXTERNAL_STORAGE permissions are being replaced with more fine-grained media specific permissions.
- StrongBox Keymaster: an implementation of the Keymaster HAL that resides in a hardware security module.
- You can now import encrypted keys securely into the Keystore using an ASN.1‑encoded key format.
- ...

This and much more that we or you might know about. Let's make sure we extend the guide on best practices and what testers should look for in terms of bad practices.

The focus will be on issues identified for the 1.2 milestone of the MSTG, which you can find [at Github](https://github.com/OWASP/owasp-mstg/milestone/2 "Milestone 1.2").

### Get your hands dirty with the Android and iOS crackmes

In the second stream, we want to focus on getting better crackmes and playground apps. In order to do this, there are a bunch of things we need to work on (in order of priority):

1. Upgrade the existing crackmes & apps to be compatible with the latest version of iOS and Android.
2. Ensure a proper build pipeline for the apps as part of the project so we can easily fix them.
3. Have newer detection mechanisms in the crackmes, for instance: make sure we have a crackme that effectively refuses to run on a rooted Android device (e.g. running Magisk)? Or make the app Frida-resilient. Or... whatever you like! Try to make cool challenging apps for other people. Just make sure it can be built and tested by the pipeline mentioned in 2.
4. Are [UnCrackable App for iOS Level 1](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/iOS/Level_01/) and [UnCrackable App for iOS Level 2](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/iOS/Level_02/) too easy for you? Do you have some ideas for a Level 3?

In this stream you get the chance to **work hand in hand with the Mobile Security team** on the [MSTG crackme apps](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes). The *defenders* will make them secure (or intentionally leave some holes) and the *attackers* will prove they can crack them using the latest techniques and available tools.

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

- For creating a better pipeline: a MacBook is recommended, but not mandatory.
- For iOS: an iOS device (preferably jailbroken). A MacBook is recommended but not mandatory.
- For Android: an Android device is highly recommended (preferably rooted). However for many tasks you can use the emulator.

The MSTG and crackmes are hosted in GitHub and can easily be edited by anyone, just a Github account is needed and knowledge on how to create a pull request.

## Outcomes

Updated iOS and Android chapters in the MSTG covering the latest security changes in iOS and Android.

## References

- [Workflow for MSTG contributions via Github](https://github.com/OWASP/owasp-mstg/#contributing)
- [Android Security](https://developer.android.com/topic/security/index.html)
- [Android Oreo](https://developer.android.com/about/versions/oreo/index.html)
- [iOS Security Whitepaper](https://www.apple.com/business/docs/iOS_Security_Guide.pdf)
- [MSTG GitHub Issues](https://github.com/OWASP/owasp-mstg/issues)
- [MSTG GitHub Project Page](https://github.com/OWASP/owasp-mstg/projects/2)
- [MSTG Hacking Playground](https://github.com/OWASP/MSTG-Hacking-Playground)
- [UnCrackable Mobile Apps](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes)
- [UnCrackable App for Android Level 1](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/Android/Level_01/)
- [UnCrackable App for Android Level 2](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/Android/Level_02/)
- [UnCrackable App for Android Level 3](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/Android/Level_03/)
- [UnCrackable App for iOS Level 1](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/iOS/Level_01/)
- [UnCrackable App for iOS Level 2](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/iOS/Level_02/)
- [UnCrackable App repository](https://github.com/commjoen/uncrackable_app)
