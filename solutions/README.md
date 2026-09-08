# Exercise Solutions

Open this directory only after attempting the exercises. The goal is to compare design decisions, not just copy a final implementation.

## Run the solutions

From the repository root:

```bash
python -m solutions.cart
python -m solutions.notifications
python -m solutions.discount
python -m solutions.policy_service
```

## Solution map

| Exercise | Solution | Main lesson |
|---|---|---|
| Shopping cart | [`cart.py`](cart.py) | Per-instance state, validation, and properties |
| Polymorphic notifications | [`notifications.py`](notifications.py) | Duck typing and behavior-based design |
| Threshold discount | [`discount.py`](discount.py) | Open/Closed Principle |
| Rating policy | [`policy_service.py`](policy_service.py) | Dependency Inversion and injected policy |

## Design notes

### Shopping cart

The cart owns its own list of prices, validates input before mutation, and calculates the total from its internal state. A property exposes the result without allowing callers to assign an arbitrary total.

### Notifications

`notify` depends only on the `send` behavior. The sender classes do not need a shared parent class, and adding a new sender does not require editing the consumer.

### Discounts

Each discount is an implementation of a small contract. A new discount can be added without expanding the checkout algorithm's conditional logic.

### Rating policies

The review model keeps its fundamental validation. The service receives an additional policy from outside, allowing stricter rules without hard-coding every rule into the service.

## Before comparing your code

Ask yourself:

1. Does invalid input fail before state changes?
2. Is each object responsible for its own state?
3. Does the consumer depend on behavior rather than concrete class names?
4. Can a new variation be added without editing stable orchestration code?
5. Are the abstractions smaller than the problem they solve?

There can be more than one correct implementation. Prefer the solution that is easiest to explain, test, and change.
