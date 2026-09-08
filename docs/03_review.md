# OOP and SOLID Review

Use this page as an active-recall checkpoint. Answer each question before opening the answers. Whenever possible, connect your explanation to a real file in `examples/` or `book_project/`.

## Questions

1. What is the difference between a class and an object? Why does an instance method receive `self`?
2. Does `__init__` create the object itself?
3. What is the difference between a class attribute and an instance attribute? Show the mutable-list trap.
4. Are `_name` and `__name` truly private in Python?
5. When is a property a better interface than direct attribute access?
6. What is the difference between encapsulation and abstraction?
7. Does polymorphism require inheritance?
8. What does `super()` do, and how is it related to the MRO?
9. When would you choose composition instead of inheritance?
10. What is the difference between an instance method, a class method, and a static method?
11. How are `ABC` and `Protocol` different? Do type annotations validate values at runtime?
12. What can a `dataclass` generate? Does `frozen=True` freeze a list stored inside the object?
13. Does SRP mean that a class may contain only one method?
14. How can you add a new discount while respecting OCP?
15. Give an LSP violation and explain which contract was broken.
16. What is the difference between SRP and ISP?
17. How are DIP and Dependency Injection different?
18. Why should the rating service return `None` when a book has no reviews?
19. How can the application prevent a review from being added to a missing book?
20. If storage changes from memory to SQLite, which parts should change?

<details>
<summary><strong>Short answers</strong></summary>

1. A class is a definition; an object is an instance. `self` identifies the current instance.
2. `__new__` creates the object. `__init__` initializes the already-created object.
3. Class attributes are shared by default; instance attributes belong to one object. A mutable list on the class can be changed by every instance.
4. `_name` is a convention. `__name` uses name mangling to reduce accidental collisions, but neither is an absolute security boundary.
5. Use a property for computed values, validation, or controlled access while preserving attribute-style syntax.
6. Encapsulation protects and organizes state. Abstraction defines the useful contract while hiding implementation details.
7. No. Duck typing and structural protocols can provide polymorphism without a shared parent class.
8. `super()` continues lookup through the next implementation in the MRO. In cooperative multiple inheritance, every class can contribute once.
9. Choose composition when an object needs replaceable behavior or when an “is-a” relationship would be misleading.
10. Instance methods receive `self`, class methods receive `cls`, and static methods receive neither automatically.
11. `ABC` provides a nominal contract; `Protocol` supports structural typing. Type hints do not automatically enforce runtime validation.
12. A dataclass can generate methods such as `__init__`, `__repr__`, and `__eq__`. `frozen=True` blocks normal field reassignment but does not freeze nested mutable values.
13. No. SRP means one cohesive reason to change, not one method.
14. Add a new discount implementation that satisfies the discount contract and keep checkout unchanged.
15. A bird base type that promises every bird can fly is broken by a penguin subtype that cannot fulfill that promise.
16. SRP concerns reasons for change inside a unit. ISP concerns the size of contracts from the consumer's perspective.
17. DIP is the direction of dependency toward abstractions. Dependency Injection is the technique of supplying a dependency from outside.
18. `None` distinguishes “no review data” from a real numeric average. Zero is a meaningful number, not absence.
19. Validate the book before writing the review and raise `LookupError` without changing repository state when it is missing.
20. Add a storage adapter that fulfills the existing contracts, test it, and change the composition in the demo. Services should remain stable.

</details>

## Final challenge

Give yourself 15 minutes:

1. Draw the relationships inside `book_project`.
2. Explain the complete `add_review(1, 5)` flow.
3. Add a new rating policy without opening the solution.
4. Explain why each responsibility belongs where it is.

You are ready to move on when you can explain **why** the design is separated, modify an example safely, and identify a broken contract without memorizing principle names only.
