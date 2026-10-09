# GPA Calculator (v1, Python)

My first programming project: a terminal program that calculates one-semester and cumulative GPA from exam marks.

> **There is a newer version:** [GPA Calculator V2](https://github.com/Berekety1/GPA-Calculator-V2) is a web app built with React. [Try it live](https://berekety1.github.io/GPA-Calculator-V2/).

## The story

When we returned to school after the COVID-19 pandemic, everyone was worried about their grades and wondering what their GPA would be, so I decided to do something about it. I asked our school counselor how GPA is calculated, and he gave me the rules. Then I started writing a program that followed them. Most students, including my friends, laughed, because they didn't think I could do it. I worked day and night over one weekend and finished the first text-based version. People were amazed. I kept improving it after that, and it became the starting point for everything I've built since.

## What it does

- **One-semester GPA** and **cumulative GPA** across several semesters
- Converts each exam mark (0–100) to grade points on a **4.3 scale**:

  | Mark | ≥ 94.5 | ≥ 89.5 | ≥ 84.5 | ≥ 74.5 | ≥ 70.5 | ≥ 65.5 | ≥ 59.5 | ≥ 49.5 | below |
  |---|---|---|---|---|---|---|---|---|---|
  | Points | 4.3 | 4.0 | 3.7 | 3.3 | 3.0 | 2.7 | 2.3 | 2.0 | 1.0 |

- Weights **main subjects** (such as maths or physics) at 0.5 credit hours and **elective subjects** (such as HPE) at 0.25
- Shows your total points, credit hours, learning hours and a "rank" message

## Run it

```bash
python gpa_calc_V1.3.py
```

Then choose from the menu:

```
1.Calculate one semester GPA
2.Calculate cumulative GPA
3.About
4.How to calculate
99.Exit
```
