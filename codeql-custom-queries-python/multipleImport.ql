import python

predicate multiple_import(Import imp) { count(imp.getAName()) > 1 and not imp.isFromImport() }

from Import i
where multiple_import(i)
select i, "Multiple imports on one line."