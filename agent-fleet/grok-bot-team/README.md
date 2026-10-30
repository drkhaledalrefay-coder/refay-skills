# Grok Bot Team

![Grok Bot Team project crew](assets/grok-bot-team.jpg)

[اقرأ الدليل بالعربية ↓](#الدليل-بالعربية)

**Turn a substantial project task into a coordinated Grok Bot team.** This skill helps Grok Bot choose useful roles, open a project room when supported, and optionally discover command-line agents on a machine registered with the connected environment.

> The skill describes a workflow, not a promise of product features. Grok Bot must check which room, agent and machine tools are available before using them.

## At a glance

| | |
| :--- | :--- |
| **Use it for** | Multi-step work that benefits from planning, production and independent review |
| **You need** | Grok Bot with the relevant connected tools; a registered machine only if you want local CLI discovery |
| **Optional** | Coding or text CLI agents installed on that machine |
| **You get** | A coordinated room when available, a plan, reviewed deliverables, and an accurate report of what actually ran |

## What it does

Grok Bot Team turns a broad request into a bounded workflow:

1. **Clarify the outcome** — restate the deliverable and ask only for missing details that affect the result.
2. **Choose the right roles** — for example, a lead, a maker and an independent reviewer.
3. **Check available teammates** — reuse suitable existing agents and create a new one only if the connected tools support it.
4. **Discover optional local CLIs** — check a registered machine with platform-appropriate commands; ask for required approval before running discovery or a CLI task.
5. **Coordinate the work** — open and brief a project room if the feature is available.
6. **Review and report** — inspect results, identify what was checked, and share only links and outputs confirmed by the tools.

## When to use it

Use the skill when a task has several parts or needs different kinds of judgment, such as:

- Building a small website or application
- Preparing a report with research and fact-checking
- Producing a campaign with writing and brand review
- Creating a video that needs editing and visual review

For a quick answer, a single edit or personal operations such as sending a message or changing a calendar, skip the project room.

## Requirements

- **Grok Bot** with whatever room, agent or machine tools are needed for the requested workflow.
- **A registered machine** available through Grok Bot if you want to discover or run local CLI agents.
- **Optional CLI tools** installed on that machine and available on PATH.

Without a registered machine, Grok Bot can still coordinate the work it can perform itself and with its available agents. Finding a command on PATH does not prove that it is signed in, licensed or ready to run.

## Install and use

Use the method supported by your Grok Bot environment:

1. Add the `grok-bot-team` folder to the supported skills location, if the environment provides one; or
2. Provide the contents of [`SKILL.md`](SKILL.md) as skill context if the client supports that.

There is no universal installer assumed by this repository. Once loaded, give Grok Bot a multi-step task and ask it to organize the work with a project team.

## Example: from request to delivery

A user asks:

> Build a three-page portfolio site for my photography work. Use the images in my project folder, make it mobile-friendly, and give me a preview link by Friday.

Grok Bot should:

1. Confirm the three-page site and Friday preview, then ask which project folder to use if that is not clear.
2. Choose a technical lead, a builder and a code reviewer, reusing existing teammates where suitable.
3. If machine access is available, check registered machines and ask for the required approval before discovering installed CLIs.
4. Open a room if supported, with the approved source folder, deliverable, deadline, constraints, roles and review order.
5. Give the builder and any approved CLI a bounded task, then inspect the work and have the reviewer check the pages and mobile layout.
6. Share a preview link only if a connected tool actually created one, and report which agents and CLIs participated.

This is an example of the intended process. It does not claim that a room was opened, a CLI was run or a preview was produced.

## Local CLI discovery

The skill includes discovery commands for Windows PowerShell and POSIX shells on macOS or Linux. They locate matching commands on PATH; they do not install tools or verify that the tools can authenticate.

Grok Bot should run discovery only through a registered machine and follow the connected tool's approval requirements. Before launching a discovered CLI, it should show the proposed command and task, get the required approval, use the user's selected project folder, and inspect the result.

## Outputs and review

Depending on the tools available, the workflow can produce:

- A focused project room and kickoff brief
- A short plan with role assignments
- Work from approved agents or CLI tools
- An independent review and list of remaining fixes
- Final deliverable links and a report of what actually ran

If a feature is unavailable, the skill requires Grok Bot to say so and continue with the parts it can do.

## Limits and privacy

- Room creation, teammate listing, agent creation and machine access depend on the connected Grok Bot environment.
- Local discovery reports commands found on PATH only. It does not prove successful execution.
- The skill does not install agents, grant permissions, bypass approvals or promise access to a particular model or service.
- The user must supply or approve project folders, local commands and external actions as required by the connected tools.
- Do not claim an agent, machine, command, upload, review or deliverable succeeded unless the relevant tool confirms it.
- Keep project-room content limited to information needed for the task and respect the user's privacy restrictions.

## الدليل بالعربية

**حوّل المهام الكبيرة إلى فريق عمل منظم داخل Grok Bot.** تساعد هذه السكيل Grok Bot على توزيع الأدوار، وفتح غرفة للمشروع إذا كانت الميزة متاحة، واكتشاف أدوات CLI الاختيارية على جهاز مسجل.

> السكيل تشرح سير عمل مقترحًا، ولا تضمن توفر ميزات بعينها. على Grok Bot التحقق من الأدوات المتاحة في اتصاله قبل استخدامها.

### متى تستخدمها؟

استخدمها في المهام متعددة الخطوات التي تستفيد من التخطيط والتنفيذ والمراجعة، مثل بناء موقع، أو إعداد تقرير بحثي، أو إنتاج حملة أو فيديو.

لا حاجة لغرفة مشروع لسؤال سريع أو تعديل واحد أو لمهام شخصية مثل إرسال رسالة أو تعديل موعد.

### المتطلبات

- **Grok Bot** مع أدوات الغرف أو الوكلاء أو الأجهزة اللازمة للمهمة.
- **جهاز مسجل** ومتاح من خلال Grok Bot إذا أردت اكتشاف أدوات CLI أو تشغيلها.
- **أدوات CLI اختيارية** مثبتة على الجهاز ومتاحة عبر PATH.

إذا لم يتوفر جهاز مسجل، يظل بإمكان Grok Bot تنسيق العمل الذي يستطيع تنفيذه بنفسه وبمساعدة الوكلاء المتاحين. العثور على أمر في PATH لا يؤكد تسجيل الدخول أو صلاحية الترخيص أو نجاح التشغيل.

### كيف تعمل؟

1. يوضح Grok Bot المطلوب والموعد والتنسيق، ويسأل فقط عن التفاصيل الناقصة التي ستؤثر في النتيجة.
2. يختار الأدوار المناسبة، مثل قائد للمهمة ومنفذ ومراجع مستقل.
3. يتحقق من الوكلاء الموجودين ويعيد استخدام المناسب منهم. لا ينشئ وكيلًا جديدًا إلا إذا كانت الأدوات المتاحة تدعم ذلك.
4. عند توفر جهاز مسجل، يكتشف أدوات CLI المناسبة لنظام التشغيل. يطلب الموافقة اللازمة قبل أوامر الاكتشاف أو تشغيل أي أداة.
5. يفتح غرفة للمشروع ويكتب ملخص البداية إذا كانت ميزة الغرف متاحة.
6. يراجع النتائج، ثم يشارك المخرجات والروابط التي تأكد منها، ويوضح ما نُفذ فعلًا.

### التثبيت والاستخدام

استخدم طريقة التثبيت التي تدعمها بيئة Grok Bot لديك:

1. أضف مجلد `grok-bot-team` إلى مكان السكيلز الذي تدعمه البيئة؛ أو
2. مرّر محتوى [`SKILL.md`](SKILL.md) إلى Grok Bot كسياق إذا كان العميل يدعم ذلك.

لا يفترض هذا المستودع وجود مُثبّت موحد. بعد تحميل السكيل، أعطِ Grok Bot مهمة متعددة الخطوات واطلب منه تنظيمها بفريق مشروع.

### مثال: من الطلب إلى التسليم

يطلب المستخدم:

> أنشئ موقعًا شخصيًا من ثلاث صفحات لأعمالي في التصوير. استخدم الصور الموجودة في مجلد المشروع، واجعل الموقع مناسبًا للجوال، وأرسل لي رابط معاينة قبل يوم الجمعة.

ينبغي أن يقوم Grok Bot بما يلي:

1. يؤكد الصفحات الثلاث وموعد الجمعة، ويسأل عن مجلد الصور إذا لم يكن محددًا.
2. يختار قائدًا تقنيًا ومنفذًا ومراجعًا للكود، مع إعادة استخدام الوكلاء المناسبين الموجودين.
3. إذا توفر جهاز مسجل، يتحقق من أدوات CLI ويطلب الموافقات اللازمة قبل اكتشافها أو تشغيلها.
4. يفتح غرفة عند توفر الميزة، ويوضح فيها المجلد المعتمد والمطلوب والموعد والقيود والأدوار وترتيب المراجعة.
5. يوزع مهامًا محددة، ثم يفحص العمل ويطلب من المراجع التحقق من الصفحات وعرض الجوال.
6. يرسل رابط المعاينة فقط إذا أنشأته أداة متصلة بالفعل، ويذكر الوكلاء وأدوات CLI التي شاركت فعلًا.

هذا مثال توضيحي لسير العمل، وليس ادعاءً بأن غرفة فُتحت أو أمرًا شُغّل أو معاينة أُنشئت.

### اكتشاف أدوات CLI

تتضمن السكيل أوامر اكتشاف لـ Windows PowerShell وصدفة POSIX على macOS وLinux. تبحث الأوامر عن الأدوات المتاحة في PATH؛ ولا تثبت برامج جديدة أو تتحقق من تسجيل الدخول.

يجب تشغيل أوامر الاكتشاف على جهاز مسجل فقط، واتباع موافقات الأداة المتصلة. قبل تشغيل أي CLI، يوضح Grok Bot الأمر والمهمة، ويحصل على الموافقة المطلوبة، ويستخدم مجلد المشروع الذي حدده المستخدم، ثم يفحص النتيجة.

### المخرجات والمراجعة

بحسب الأدوات المتاحة، قد ينتج عن سير العمل:

- غرفة مشروع وملخص بداية.
- خطة قصيرة وتوزيع للأدوار.
- مخرجات من الوكلاء أو أدوات CLI المعتمدة.
- مراجعة مستقلة وقائمة بالإصلاحات المتبقية.
- روابط التسليم وتقرير يوضح ما تم تشغيله فعلًا.

إذا لم تتوفر ميزة، يجب على Grok Bot توضيح ذلك ومتابعة الأجزاء الممكنة.

### الحدود والخصوصية

- إنشاء الغرف والوكلاء، واستعراض أعضاء الفريق والوصول إلى الأجهزة تعتمد على الأدوات المتاحة في بيئة Grok Bot المتصلة.
- اكتشاف CLI يعرض الأوامر الموجودة في PATH فقط ولا يثبت نجاح تشغيلها.
- السكيل لا تثبت وكلاء، ولا تمنح صلاحيات، ولا تتجاوز الموافقات، ولا تضمن الوصول إلى نموذج أو خدمة بعينها.
- على المستخدم تحديد مجلدات المشروع والموافقة على الأوامر والإجراءات الخارجية حسب متطلبات الأدوات المتصلة.
- لا تدّعِ نجاح تشغيل وكيل أو جهاز أو أمر أو رفع ملف أو مراجعة إلا بعد تأكيد الأداة المعنية.
- اجعل محتوى غرفة المشروع محدودًا بما يحتاجه العمل، واحترم تعليمات الخصوصية التي يحددها المستخدم.

---

## Folder contents

- [`SKILL.md`](SKILL.md) — the instructions Grok Bot follows.
- [`README.md`](README.md) — overview, installation guidance and example.
- [`assets/grok-bot-team.jpg`](assets/grok-bot-team.jpg) — the team illustration shown above.

## License

This skill is part of [Refay Skills](../../README.md) and follows its [CC BY 4.0 license](../../LICENSE).
