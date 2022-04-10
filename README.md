This package includes various utility modules I find useful.

# pcolrm

```
Usage: pcolrm [OPTIONS] COL_NUMS

  Remove columns from a file.

  This utility mimics what colrm does. One of the differences is that columns
  are separated by delimiters instead of each single character representing
  one column.

  Like colrm, this utility reads its input from the standard input and writes
  its output to the standard output.

  COL_NUMS is a list of comma separated column numbers that are to be removed.
  You can use '-' to specify a range. For example, 1,2,4 or 1-2,4 etc.

  Column numbering starts with one, not zero.

Options:
  -d, --delimiter TEXT  Delimiter.  [default:  ]
  --help                Show this message and exit.
```

