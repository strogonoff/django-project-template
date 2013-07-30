Development guidelines
======================

- `A Foolish Consistency is the Hobgoblin of Little Minds <http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds>`_ applies
  regardless of language.
  Look at code around and make your code consistent.

Writing Python
--------------

- Make sure the code you write adheres to `PEP 8`_, including the
  consistency part (do not change style of code around, instead write
  your code to be consistent with it).

- Write docstring before you write the definition.

- Run tests before you make changes---what if tests are failing in master
  and no one has noticed? Before you commit changes it's good to run tests,
  too, to make sure CI builds won't break after you push.

- Write tests for your changes. If it's hard to test your code, consider
  restructuring it---usually well-designed code is easy to test.

- Use pylint.

.. _development-writing-javascript:

Writing JavaScript
------------------

- Keep your code JSLint-compliant.

- Follow `conventions suggested by Douglas Crockford <http://javascript.crockford.com/code.html>`_.

Writing CSS
-----------

- Code structure follows `CSS architecture <http://engineering.appfolio.com/2012/11/16/css-architecture/>`_.
