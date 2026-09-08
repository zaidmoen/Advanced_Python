# Exercises — Build Before You Read the Solution

These exercises are intentionally small. Read the requirement, write the code, test the edge cases, and only then compare your work with [`solutions/`](../solutions/).

## Exercise 1 — `ShoppingCart`: state and encapsulation

Create a cart with:

- `add(price)` for adding a price in integer cents;
- a read-only `total` property;
- validation that rejects booleans, fractions, negative values, and non-integers.

Acceptance criteria:

```python
cart = ShoppingCart()
cart.add(100)
cart.add(250)
assert cart.total == 350
```

Create a second cart and verify that changing the first cart does not change the second one. Adding `-1` must raise `ValueError` and leave the total unchanged.

Reference: [`solutions/cart.py`](../solutions/cart.py).

## Exercise 2 — Polymorphism without inheritance

Create `EmailPreview` and `SmsPreview`. Each object must provide:

```python
send(message)
```

The method should return a preview string and must not perform real delivery.

Then write one function:

```python
def notify(sender, message):
    return sender.send(message)
```

The function must work with both senders without `isinstance` checks or type-specific branches. Add `PushPreview` without modifying `notify`.

Reference: [`solutions/notifications.py`](../solutions/notifications.py).

## Exercise 3 — OCP: add a discount

Start from the OCP example and create `ThresholdDiscount` with this behavior:

| Price | Result |
|---:|---:|
| 999 | 999 |
| 1000 | 900 |
| 1200 | 1100 |

Do not modify the checkout algorithm. Add the new discount as another implementation of the existing contract.

Reference: [`solutions/discount.py`](../solutions/discount.py).

## Exercise 4 — A book rating policy

Add a `RatingPolicy` contract with:

```python
validate(rating)
```

Update `ReviewService` so it receives the policy as a dependency.

Implement two policies:

1. A default policy that accepts ratings from 1 through 5.
2. A stricter policy that accepts ratings from 3 through 5.

Keep the basic `Review` validation. A rejected rating must never be stored. Use the same service with both policies.

The goal is to practice OCP and DIP, not to distribute conditionals across unrelated files.

Reference: [`solutions/policy_service.py`](../solutions/policy_service.py).

## Quick tracing questions

1. If `skills` is a class-level list, what happens when two objects modify it?
2. If a repository returns its internal review list directly, how can a caller corrupt its state?
3. If `ReviewService` creates `MemoryReviewRepository` internally, why is testing harder?
4. Do type hints stop an invalid object from being passed at runtime? Prove your answer with a small experiment.

## Completion checklist

- [ ] The happy path works.
- [ ] Invalid input raises the intended exception.
- [ ] Failed operations do not partially mutate state.
- [ ] The consumer does not need type-specific branching.
- [ ] You can explain which SOLID principle the exercise demonstrates.
