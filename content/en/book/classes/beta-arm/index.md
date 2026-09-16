---
title: "Sorting arm — beta"
summary: "Unlisted preview of the animated banner proposed for the Courses page."
type: docs
math: true
noindex: true
_build:
  list: never
  render: always
---

## Beta preview

Not linked from anywhere and kept out of search engines — it exists so the banner can be
looked at inside the real site, with the real theme, the real logos and the dark-mode
toggle in the navbar. Nothing on the live Courses page has changed.

### Option 1 — the three schools

{{< sorting-arm bins="CENTRALE/RL|ECE/CONTROL|ALBERT/MATHS" >}}

This is the banner as it would sit at the top of [Courses](../), above the three school
cards:

<div class="school-cards">

<a class="school-card" href="../centralesupelec/">
  <div class="school-logo"><img src="../assets/logo-centralesupelec.png" alt="CentraleSupélec"></div>
  <div class="school-card-name">CentraleSupélec</div>
  <div class="school-card-desc">Reinforcement Learning</div>
</a>

<a class="school-card" href="../ece/">
  <div class="school-logo"><img src="../assets/logo-ece.webp" alt="ECE Paris"></div>
  <div class="school-card-name">ECE Paris</div>
  <div class="school-card-desc">Sampled Control Systems</div>
</a>

<a class="school-card" href="../albertschool/">
  <div class="school-logo"><img src="../assets/logo-albertschool.png" alt="AlbertSchool"></div>
  <div class="school-card-name">AlbertSchool</div>
  <div class="school-card-desc">Mathematics Foundations</div>
</a>

</div>

### Option 2 — one school, three topics

The same machine sorting three copies of the ECE logo into the three blocks of the
Sampled Control course, for the [ECE page](../ece/) rather than the Courses hub.

{{< sorting-arm logos="../assets/logo-ece.webp|../assets/logo-ece.webp|../assets/logo-ece.webp" bins="Z-TRANSFORM/SESSION 5|SAMPLED PID/SESSION 7|KALMAN/SESSION 9" >}}

### Notes

Everything is simulated rather than keyframed: closed-form two-link inverse kinematics on
the elbow-up branch, each joint tracked by a PD law at $k_p = 70$, $k_d = 13.5$ — so
$\omega_n \approx 8.4$ rad/s and $\zeta \approx 0.81$, and the small overshoot as the claw
arrives is the controller settling. A parallelogram wrist keeps the head level, the claw
opens above the bin and the logo falls under gravity, and the eyes lead the motion toward
whatever the arm is reaching for next.

The banner pauses itself when it scrolls out of view, honours
`prefers-reduced-motion` (one composed still plus a play button), and has a pause control
in its bottom-right corner.
