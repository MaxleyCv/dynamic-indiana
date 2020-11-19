# Practical work IoT #4
An implementation of the task ijones on dynamic programming (practical work #4)

# Indiana Jones task
Iндiана Джонс i останнiй прямокутний обхiд

В пошуках Святого Грааля Iндiана Джонс зiткнувся з небезпечним випробуванням.
Йому потрiбно пройти крiзь прямокутний коридор, який складається з крихких плит
(пригадайте сцену з фiльму «Iндiана Джонс i останнiй хрестовий похiд»). На кожнiй
плитi написана одна лiтера:

Можна починати з будь-якої плити в найлiвiшому стовпцi. Виходом iз коридору є
верхня права та нижня права плити (для прикладу вище — a та f).
Iндiана спритний, i може переходити не лише на сусiдню плиту, а й перестрибувати
через кiлька плит. Проте, щоб не провалитися крiзь пiдлогу, вiн повинен дотримуватися
таких правил:  
a a a  
c a b  
d e f  

1. Пiсля кожного кроку Iндiана повинен опинятися правiше, нiж був перед цим.

2. Завжди можна переходити на одну плиту праворуч.

3. Крiм руху на одну плиту праворуч, можна перестрибувати, проте лише на ту
саму лiтеру. Наприклад, з лiтери a можна перестрибнути на будь-яку iншу
лiтеру a за умови, що ми цим ходом просунемося правiше.

Для заданого коридору, пiдрахуйте, скiльки всього iснує способiв пройти його успiшно.

### Вхiднi данi
Вхiдний файл ijones .in складається з H + 1 рядкiв.
• Перший рядок мiстить два числа W i H, роздiленi пробiлом: W — ширина
коридору, H — висота коридору, 1  W, H  2000.
• Кожен з наступних H рядкiв мiстить слово довжиною W символiв, яке складається
з малих латинських лiтер вiд a до z.

### Вихiднi данi
Вихiдний файл ijones .out повинен мiстити одне цiле число — кiлькiсть рiзних
шляхiв для виходу з коридору

## In a nutshell
Find a sum of all possible paths from leftmost column of the matrix   
to top right and bottom right cell.
Every cell has a tag (a-z).
There are 3 rules:  
- every time we go right
- we can go one cell right
- we can go on any cell with the same tag as a current
### Input example
```
7 6
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
```
### Output example
```201684```
# Manual
- modify your input and output files in ```utils/utils.py```
- add the test case to your input file
- run ```python main.py``` in the root directory