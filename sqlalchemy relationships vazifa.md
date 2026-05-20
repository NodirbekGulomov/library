1. `Author` va `Book` modellari yarating.

`Author`:

* id  
* full\_name  
* birth\_year

`Book`:

* id  
* title  
* price  
* published\_year  
* author\_id

---

2. `One-to-Many relationship` tashkil qiling.

Talab:

* Bitta author ko‘p book yozishi mumkin  
* Har bir book faqat bitta authorga tegishli bo‘lsin

`relationship()` va `ForeignKey` ishlating.

---

3. SQLite database yarating (`library.db`).

---

4. Databasega kamida:  
* 5 ta author  
* har bir authorga kamida 2 tadan book

qo‘shing.

---

5. Quyidagi querylarni yozing:  
* Barcha authorlarni chiqaring  
* Barcha booklarni chiqaring  
* Har bir author va uning booklarini chiqaring  
* Faqat ma’lum bir authorning booklarini chiqaring  
* Narxi 100000 dan katta bo‘lgan booklarni chiqaring  
* 2015-yildan keyin chiqqan booklarni chiqaring  
* Eng qimmat bookni chiqaring  
* Eng ko‘p book yozgan authorni toping  
* Har bir authorda nechta book borligini chiqaring  
* Book nomida `"Python"` so‘zi qatnashganlarini filter qiling  
* Bookni author nomi bilan birga chiqaring

Masalan:

Clean Code \-\> Robert Martin

**2-topshiriq.** Python list data type mavzusida 10 minutlik video tushuntirish yozing yoki maqola yozing.

Maqsad videoni korgan yoki maqolani oqigan odam pythonda list data typeni bemalol mustaqil foydalana oladigan va tushunadigan darajaga yetishi kerak.