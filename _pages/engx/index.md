---
title: Engineering Excellence
banner_src: ./img/banner.jpeg
---

<img alt="" src="./img/purple-blue-banner.png" />

_Note: this page is generated from a markdown file for the most part._

Welcome to the Engineering Excellence handbook. This guide forms part of a wider
initiative to improve the quality of the software we produce at IBM. Improving
our awareness of, and our expertise in, modern software practices is a crucial
step towards delivering better software to our customers more efficiently.
Greater efficiency cannot be achieved by simply 'working harder', it is achieved
by adopting best-in-class tools and methods to reduce errors and rework. The
ambition is to find defects in the software we produce closer to the point of
injection and to optimize our delivery pipelines.

Testing is a cornerstone in our approach to quality assurance. This guide brings
together a collection of guidelines and good practices we believe are essential
for high performing to embrace, along with examples and recommendations of how
to adopt and implement them.

In order to ensure a common approach across IBM's software portfolio, the new
Engineering Excellence Assessments (abbreviated as the `EngX assessments`
throughout this guide) provide a way for teams to benchmark their delivery
engine.

## Why testing?

Testing is an integral part of software delivery and critical to IBM's
reputation. While it's unlikely that many would disagree with that statement,
how we approach testing can have a significant impact on outcomes and the speed
at which we can deliver value to customers. As software delivery practitioners,
there are two aspects to quality that we must get right: correctly aligning our
testing with customer utilization and isolating key defects as early as we can.
IBM has a strong reputation for support, but even with the best support in the
world, the cost of a major escape in the field could be catastrophic to the
business. The chart below illustrates how the cost of defect fixing grows from
the point of injection to a critical outage in the field. There is no upper
limit to the impact as reputational damage could permanently tarnish a brand.
This is the primary motivation for the industry mantra 'shift left'.

![The cost of poor quality](./img/why-test-graph.png)

Three-in-a-box teams are collectively responsible for delivering the 'right
thing' and delivering the 'thing right'. While testing seeks to validate both of
these aspects, this assessment primarily focuses on the latter: the
effectiveness and efficiency of the engineering pipeline. The tests that the
delivery engine execute should adequately critique the product and this guide
additionally aims to share good practice. This is often referred to as delivery
engine speed versus delivery engine power. A quick engine can get the job done
quickly, while a powerful engine does a good job. Critically, the quest for
speed should not compromise power, the ambition is to remove waste and
inefficiencies that limit available power.

The delivery pipeline should be front and center of what a delivery team does.
It's fundamental, and without it the delivery team can't get value out of the
door. Completing an assessment should be viewed as a positive exercise. It
provides an opportunity for the team to assess the health of their pipeline and
ensure it is 'fit for purpose', and will continue to serve the team into the
future.

Good testing allows teams to write code with more confidence, which in turn
makes them more productive and able to shift focus on delivering new features
and value to our customers.

## Where to start?

Getting started can be the hardest part of any journey, and it can be easy to
get distracted by the complexity of a modern software delivery pipeline. Let's
take a step back. Software development starts with a code change entering the
delievry pipeline. The T2 metrics chart below provides a high level snapshot
what a pipeline does.

![T2 metrics](./img/t2-metrics-chart.png)

Let's start by asking some basic questions of our pipeline. For a given code
change:

- How quickly can I go through the steps to get a build and a signal back from
  appropriate tests that the change is good or bad? This unit of time is Time to
  Known Result (T2KR).
- How quickly can I go through the steps to get a build, rework a defect from a
  test failure and know my code change is good? This unit of time is Time to
  Known Quality (T2KQ)
- How quickly, on average, can I go through the steps to get a build and go
  through all the stages before I can ship my code change to a customer? This
  unit of time is Time to Quality (T2Q).
- How many steps in the pipeline take a long time e.g., days (enough time for a
  skiing holiday)? How many of the steps happen in a few minutes(enough time for
  a tea break)? What would it take to move the pipeline from Ski to Tea?

Spending a few minutes as a team thinking about the T2 metrics can be a really
useful place to start. It helps visualize what's going on under the covers and
provides context for the assessment process.

## What is expected from you?

### → Managers

Your role is to become familiar with the goals and process of this initiative,
especially the EngX assessment itself. You will need to facilitate the EngX
assessment process within your team by allocating people, and time in the
schedule, to do it.

We want you to understand the competitive advantage efficient and automated
testing will bring to your team and to your product. We need you to understand
the level of maturity of our competition. Just because the engine is running
doesn't mean we should assume it's running well.

We expect you to actively support this initiative by providing your team with
the resources required to implement improvements. Project MaX has taken into
consideration that there will be upfront cost to teams embracing EngX. Some
teams who are lower on the maturity level will have more work. To help you
understand the maturity of your team alongside candidate improvements,
consultancy is available via an EngX SME team. Support will be prioritized by
senior management given business priorities.

### → Technical leaders

Software testing is the engineering discipline of detecting and isolating
software failures (defects). Finding 'bugs' can be easy, finding success
threatening defects is non-trivial and requires teams to invest in expertise.
Software engineers should actively research and develop tests and strategies
that prove capability and isolate failures in achieving desired outcomes.
Testing software end-to-end is a complex problem and will likely include
multiple interaction between components inside, and outside the delivery team's
control. Testing is a journey towards reducing risk. A 'fit for purpose'
delivery pipeline helps focus engineering time and expertise on product quality
and away from lower-value tasks that simply keep the engine running. How much of
your available technical resource serves the delivery pipeline? How could new
features or greater automation in the pipeline improve your ability to deliver?

As technical leaders, testing is an integral part of your delivery journey and
not something to be done just before the end. Championing code that's designed
for testing and investing in 'test skill' empowers teams to be more resilient
and autonomous. Avoiding technical debt by removing ineffective process steps
improves morale, productivity and allows you to focus more on your primary goal:
delivering features that delight your users.

The EngX assessments are not here to give you a personal grade, but rather to
start a discussion to identify area(s) for investment and improvement. Your
support in this process will guide and unify your teams.

### → Developers

As a developer, you understand that untested, or poorly tested, code is risk:
it's potential for a problem to happen. Small units of change, the ability to
contribute tests easily and a rapid feedback loop help mitigate risk stored in
the system. It's therefore important that you understand what an EngX assessment
is and why it matters. Does the pipeline deliver these characteristics? How
could new features or greater automation in the pipeline improve your confidence
in delivering great code?

### → QA / Test engineers

Test engineers apply deep knowledge and expertise in developing approaches to
isolate mission critical defects. Often engaged in exploratory testing and test
architecture, this community are often the first-responders to resolve pipeline
problems. Left unchecked, an unhealthy pipeline can consume engineering resource
in serving day-to-day chores. How could new features or greater automation in
the pipeline support you?

Again, the EngX assessments are not here to give you a personal grade, it's your
opportunity to shine light on the delivery engine and signpost where investment
will drive improvements. The whole team should be proud of the pipeline that
delivers the product alongside the product itself.
