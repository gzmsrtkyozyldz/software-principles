**SRP (Single Responsibility Principle)**

Single Responsibility Principle (SRP) is one of the SOLID principles of software design. It states that a class should have only one reason to change, meaning it should have only one responsibility or job.

Applying the SRP principle helps to create more cohesive and loosely coupled code, making it easier to understand, test, and maintain in the long run.

**DRY vs WET Principles**

The DRY (**Don't Repeat Yourself**) and WET (**Write Everything Twice, or We Enjoy Typing**) principles are two contrasting approaches to software development. They emphasize different aspects of code organization and maintenance. Here's an overview of the key differences between them:

**_DRY Principle:_**

DRY promotes code reuse and maintainability by avoiding redundancy.
It suggests that each piece of knowledge or functionality should have a single, unambiguous representation in the code.
DRY encourages modularization and abstraction to eliminate duplication.
By adhering to DRY, developers aim to reduce the potential for errors and make changes or updates easier to implement.
DRY supports the principle of having a single source of truth for a particular concept in the codebase.

**_WET Principle:_**

WET humorously suggests that it's acceptable to repeat code or information in multiple places.
It implies that code duplication is not necessarily a bad thing and may even have advantages in some cases.
WET may be employed when the repeated code is relatively small, doesn't change frequently, or has a different context in each occurrence.
WET can provide flexibility and readability, especially when the repeated code differs in subtle ways that are better expressed explicitly.
However, WET can lead to maintenance issues, as changes or updates may need to be made in multiple places, increasing the risk of inconsistencies or errors.

_In summary_, the DRY principle advocates for minimizing redundancy and maintaining a single source of truth, while the WET principle suggests that some duplication may be acceptable depending on the context. **DRY** promotes code reuse, simplicity, and ease of maintenance, whereas **WET** allows for more flexibility but increases the risk of inconsistencies and maintenance difficulties.

**SoC Principle**

The term "SoC" stands for Separation of Concerns, which is a software design principle that encourages breaking a system down into distinct parts, each addressing a separate concern or responsibility. This principle promotes modularity, maintainability, and reusability in software development.


