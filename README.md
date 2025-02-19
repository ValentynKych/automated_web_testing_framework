# Automated web testing framework

## 📚 Description

This project was created as part of learning automated testing using:

- **Selenium WebDriver** for interacting with web pages.
- **Pytest** for writing and running tests.
- **Page Object Model (POM)** for structuring code and improving its readability and maintainability.
- **Pytest fixtures** for efficiently managing common preconditions and cleanup after tests.
- **Negative checks** (functions like `is_not_*`) for verifying the absence of elements or text.
- **Test organization**, where test functions are structured similarly to traditional test cases.

## 📝 Features

- 📄 **Page Object Model**: each web application page has a separate class describing its elements and interaction methods.
- 🧪 **Pytest fixtures**: used to manage the browser lifecycle and other shared resources.
- ⚡ **Negative checks**: methods such as `is_not_element_present` that verify the absence of elements on the page.
- 🚦 **Flexible test management**: use of `@pytest.mark.skip` with a clear reason for skipping tests.

## ⚠️ Note

Some tests are marked with `@pytest.mark.skip` because their proper implementation depends on additional requirements (e.g., text localization or content verification strategy).

## 💡 What I Learned

- Effective use of Selenium and Pytest for writing automated tests.
- Implementation of the Page Object Model architecture for better project maintainability.
- Writing negative tests and validations.
- Using fixtures to minimize repetitive code.
- Organizing tests in a way that closely resembles traditional test cases.

---

✨ *Thank you for checking out the project!* 🚀

