---
title        : Creating content session
type         : working-session    # working-session, user-session
track        : OWASP MSTG
technology   : Mobile, iOS, Android
categories   : MSTG                   # GDPR, Juice Shop, etc.
featured     : yes                # review with summit team "yes"
when_day     : Mon, Tue, Wed, Thu, Fri
when_time    :
room_layout  :                    #
room_id      :
session_slack:
status       : review-content              # draft, review-content, done
organizers   : Jeroen Willemsen, Carlos Holguera
description  : Updating the content of the MSTG
participants : Jeroen Willemsen, Sven Schleier (remote), Abderrahmane AFTAHI (remote), Carlos Holguera
---

Welcome to the OWASP Mobile Security Testing Guide Content pressure cook!

## Why

Staying up-to-date is key, especially regarding mobile security. We have the chance to do it all together in the same place. In this working session we will go through and discuss about the latest security features introduced in the latest Android and iOS versions. We go not only theoretical but also practical: we have of course a hands-on part for this working session where we will be playing and enhancing the MSTG Hacking Playground and crackme apps. So get your phones, laptops and favorite tools ready.

## What

### Get to know the latest Android and iOS security enhancements

iOS 12:

- UIWebViews are officially deprecated
- new AuthenticationServices and Network Frameworks
- New Password AutoFill Framework for iOS and web apps
- ...

Android 9:

- Scoped Storage: an isolated storage sandbox right on external storage device! The READ_ and WRITE_EXTERNAL_STORAGE permissions are being replaced with more fine-grained media specific permissions.
- StrongBox Keymaster: an implementation of the Keymaster HAL that resides in a hardware security module.
- You can now import encrypted keys securely into the Keystore using an ASN.1‑encoded key format.
- ...

This and much more that we or you might know about. Let's discuss about how we can test the new features.

### Get your hands dirty with the Android and iOS crackmes

- Would you say you could write an app that effectively refuses to run on a rooted Android device (e.g. running Magisk)?
- Do you think you could stop someone using Frida from stealing your precious app data? Or at least make him/her give up trying ;)
- Do you love to code Android/iOS apps? What about writing some code to challenge other people?
- Are [UnCrackable App for iOS Level 1](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/iOS/Level_01/) and [UnCrackable App for iOS Level 2](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes/iOS/Level_02/) too easy for you? Do you have some ideas for a Level 3?

In this session you get the chance to work hand in hand with the Mobile Security team on the [MSTG crackme apps](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes). The *defenders* will make them secure (or intentionally leave some holes) and the *attackers* will prove they can crack them using the latest techniques and available tools. Aren't you curious about how other people would solve the different challenges you implement? Reverse engineering? debugging? code injection? everything is allowed.

In this session you'll get to work on tickets regarding these kind of topics and many more. See the [MSTG GitHub Issues](https://github.com/OWASP/owasp-mstg/issues) and the [MSTG GitHub Project Page](https://github.com/OWASP/owasp-mstg/projects/2) for more details.

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

- For iOS: an iOS device (preferably jailbroken). A MacBook is recommended but not mandatory.
- For Android: an Android device is highly recommended (preferably rooted). However for many tasks you can use the emulator.

## Outcomes

An updated iOS and Android chapter in the MSTG that covers the latest security changes in iOS 11/12 and Android O/P. The MSTG is hosted in Github and can easily be edited by anyone, just a Github account is needed and knowledge on how to create a pull request.


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
