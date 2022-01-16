## Taskwiki Fork

This is a fork of [tools-life/taskwiki](https://github.com/tools-life/taskwiki) except for a single difference:

When hitting Return (<CR>) on a task, it delegates to a function named `TaskSearch`. That function is not defined in this fork. Mine looks something like this:

```vim
function TaskSearch()
  let line = getline('.')
  let task_id = split(line, "#")[1]
  let task_note = trim(system('task _get  "' . task_id . '".uuid'))
  execute printf("e ./tasks/%s.md", task_note)
endfunction

command! TaskSearch :call TaskSearch()
```

Which basically creates a vimwiki file under `./tasks/$TASK_ID.md`

Many thanks to https://github.com/tools-life/taskwiki/issues/217 for providing the base code.


# Better ways of doing this
Feel free to suggest better ways of doing this. 

One idea I have i that one can remap `<CR>` and reimplement all that logic taskwiki already does again, which wouldn't require a fork. But too much work.
