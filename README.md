# xlf-merge

Tool to merge XLF translation files.
And it can also find dupes in XLF files.

## Usage

### Merging

```
xlf-merge merge <old_translation_file> <new_translation_file> <output_file> --method='source/id'
```

Merge files by source:

```bash
xlf-merge merge messages.cs.xlf.old messages.xlf messages.cs.xlf --method='source'
```

Merge files by id:

```bash
xlf-merge merge messages.cs.xlf.old messages.xlf messages.cs.xlf --method='id'
```

### Finding dupes
```
xlf-merge dupes <file_to_check> --method='source/id/target'
```

Finding dupes by source:

```
xlf-merge dupes messages.cs.xlf --method='source'
```

Finding dupes by id:

```
xlf-merge dupes messages.cs.xlf --method='id'
```

Finding dupes by target:

```
xlf-merge dupes messages.cs.xlf --method='target'
```