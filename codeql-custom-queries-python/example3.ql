/**
 * @name Command Injection Detection
 * @description Detects potential command injection vulnerabilities.
 * @kind problem
 * @problem.severity error
 * @tags security, injection, command-injection
 */
import python

from FunctionDef func
select func, "Found a function definition."
