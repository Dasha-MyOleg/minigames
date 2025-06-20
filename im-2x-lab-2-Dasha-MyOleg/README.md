## Лабораторна #2: Calculator
**ПІБ:** Дар'я Іванівна  
**Група:** ІМ-24  

---

### 1. Опис проєкту
Реалізація спрощеного клавішного калькулятора, який підтримує:
- Введення цифр (0-9).
- Арифметичні операції: додавання (`+`), віднімання (`-`), множення (`*`), ділення (`/`).
- Виконання операцій після натискання клавіші `=`.

---

### 2. Робота з гілками

Проєкт використовує одну основну гілку:
- **Головна гілка (`main`)**:  
   - Всі зміни інтегруються в цю гілку після перевірки.  
   - GitHub Actions автоматично перевіряє тести при кожному `push` або `pull request`.

---

### 3. Файли в проєкті

1. **[src/calculator.py](src/calculator.py)**: Основний код калькулятора.
2. **[input.txt](input.txt)**: Вхідний файл із послідовністю клавіш для калькулятора.
3. **[output.txt](output.txt)**: Вихідний файл із результатом обчислень.
4. **[tests/](tests/)**: Тести для перевірки основних функцій програми.


---

### 4. Інструкції для запуску

#### **Запуск програми**
1. Помістіть у файл `input.txt` послідовність клавіш. 



**Приклад вмісту `input.txt`:**
1 2 * 3 - 4 / 2 + 8=



2. Запустіть програму:
   ```bash
   python src/calculator.py
Результат обчислень буде збережено у файл output.txt.