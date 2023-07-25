# PrairieLearn Course Repository

This repository is a bare-bones PrairieLearn course repository for the purposes of individual course development.

## Fork this repository

Each of the staff members working on this project will **fork** this repository into their own account, and will use it for their own individual question development.
The forked repositories should remain **private**.

## Welcome to PrairieLearn! 

The content for your course is stored within this repository.
You can see and edit a live version at [https://prairielearn.com](https://prairielearn.com)

### Getting Started

Learn how to create your first questions and assessments using our [Get Started](https://prairielearn.readthedocs.io/en/latest/getStarted/) tutorial.

## Firas' instructions

- start in `~/Sync/EL/OPB`
- launch docker container:
    ```
    docker run -it --rm -p 3000:3000 -v ~/Sync/EL/OPB/course_dev/pl-opb-ind100:/course prairielearn/prairielearn
    ```
- Move a question you're working on in `course_dev`, and then run the following command from `~/Sync/EL/OPB`

    ```
    python physics/instructor_physics_bank/scripts/checkq.py course_dev/q01_multiple-choice/q01_multiple-choice.md --output_root=course_dev/pl-opb-ind100/questions/FM 
    ```