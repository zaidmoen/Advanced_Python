# تمارين — حاول قبل فتح الحل

## 1. ShoppingCart: الحالة والتغليف

اكتب كلاس سلة يحتوي `add(price)` وproperty اسمها `total`. الأسعار integer cents غير سالبة؛ ارفض bool والكسور والسالب.
اعمل سلتين وتأكد أن إضافة سعر للأولى لا تغيّر الثانية. إضافة 100 و250 تعطي total = 350.
إضافة -1 ترمي ValueError وتبقي total = 350. حل قابل للتشغيل في solutions/cart.py.

## 2. Polymorphism بدون وراثة

اعمل `EmailPreview` و`SmsPreview`، لكل واحد `send(message)` يرجّع نصاً فقط بدون إرسال حقيقي.
اكتب `notify(sender, message)` واحدة تستخدم الاثنين بدون isinstance أو if حسب النوع.
أضف `PushPreview` بدون تعديل notify. الحل: solutions/notifications.py.

## 3. OCP: خصم جديد

ابدأ من أمثلة OCP. اكتب `ThresholdDiscount.apply(price)`:
إذا السعر >= 1000 اخصم 100، غير هيك رجّع نفس السعر. لا تعدّل checkout.
توقع: 999 ← 999، 1000 ← 900، 1200 ← 1100. الحل: solutions/discount.py.

## 4. مشروع الكتب: سياسة قبول التقييم

أضف `RatingPolicy` بعقد validate(rating)، وخلّي ReviewService تستقبل السياسة.
التنفيذ الافتراضي يقبل 1–5، وتنفيذ ثانٍ يقبل 3–5. حافظ على تحقق Review الأساسي.
استعمل نفس service مع السياستين. التقييم المرفوض لا يُخزّن.
الهدف: OCP وDIP، مش توزيع if على عدة ملفات. الحل الكامل: solutions/policy_service.py.

## أسئلة تتبّع سريعة

1. لو skills قائمة على الكلاس، شو بصير بين نسختين؟
2. لو أرجعت self._reviews مباشرة، كيف ممكن المستخدم يعدّل الحالة الداخلية؟
3. لو ReviewService أنشأت MemoryReviewRepository داخلها، شو بصعّب الاختبار؟
4. هل type hint يمنع تمرير object غلط وقت التشغيل؟ جرّب بمثال صغير.
