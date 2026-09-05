# Advanced Python — OOP & SOLID

مراجعة عملية بالبايثون: افهم الفكرة، شغّل المثال، عدّل عليه، ثم حل التمرين بدون فتح الحل.
الشرح بالعربي والمصطلحات والكود بالإنجليزي لتقدر تناقشهم مع المدربة.

## التشغيل

تحتاج Python 3.10 أو أحدث فقط، بدون مكتبات خارجية. الأوامر من داخل مجلد الريبو.
على Windows استخدم `py` بدل `python` إذا لزم.

```bash
git clone https://github.com/zaidmoen/Advanced_Python.git
cd Advanced_Python
python examples/oop/01_classes.py
python examples/oop/02_encapsulation.py
python examples/oop/03_inheritance.py
python examples/oop/04_abstraction.py
python examples/oop/05_composition.py
python examples/oop/06_python_tools.py
python examples/solid/01_srp.py
python examples/solid/02_ocp.py
python examples/solid/03_lsp.py
python examples/solid/04_isp.py
python examples/solid/05_dip.py
python -m book_project.demo
python -m unittest discover -s tests -v
```

## مسار الدراسة

| الترتيب | الموضوع | التطبيق |
|---|---|---|
| 1 | [أساسيات OOP](docs/01_oop.md) | أمثلة 01–02 ثم تمرين 1 |
| 2 | الوراثة والتجريد والتركيب | أمثلة 03–06 ثم تمرين 2 |
| 3 | [مبادئ SOLID](docs/02_solid.md) | خمسة أمثلة قبل وبعد ثم تمرين 3 |
| 4 | [مشروع الكتب](book_project/README.md) | شغّله وتتبع مسار البيانات ثم تمرين 4 |
| 5 | [مراجعة المدربة](docs/03_review.md) | جاوب بصوتك ثم راجع الإجابات |

[التمارين](exercises/README.md) ← جرّب أولاً ← [الحلول](solutions/README.md).
المشروع تعليمي والبيانات في الذاكرة؛ تختفي لما تسكّر البرنامج.
