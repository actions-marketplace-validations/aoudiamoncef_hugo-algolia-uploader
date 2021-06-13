# Hugo Algolia Uploader

![build](https://github.com/aoudiamoncef/hugo-algolia-uploader/workflows/build/badge.svg)
![license](https://img.shields.io/github/license/aoudiamoncef/hugo-algolia-uploader)

Hugo Algolia Uploader enables you to upload your hugo algolia index file automatically.

For generic usage please see [Algolia Uploader ](https://github.com/wangchucheng/algolia-uploader).

## Try Hugo Algolia Uploader

You can use the following example as a template to create a new file with any name under `.github/workflows/`.

```yaml
name: <action_name>

on: 
  - push

jobs:
  upload_hugo_algolia_index:
    runs-on: ubuntu-latest
    name: Upload Hugo Algolia Index
    steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0
    - uses: aoudiamoncef/hugo-algolia-uploader@main
      with:
        # Such as `LAHZOUZT15`. Required
        app_id: <your_app_id>
        # You can store token in your project's 'Setting > Secrets' and reference the name here. Such as ${{ secrets.ALGOLIA_ADMIN_KEY }} . Required
        admin_key: <your_admin_key>
        # The index name. Required
        index_name: <your_index_name>
        # The index name separator. If multi languages is enabled. Default value is`_` 
        index_name_separator: <your_index_name_separator>
        # The index file directory relative to repo root. Default value is `public`
        index_file_directory: <your_index_file_directory>
        # The index file name. Default value is `index.json`
        index_file_name: <your_index_file_name>
        # The indexes i18next language codes comma separated. Ex: en,fr,tzm will upload to 3 indexes with predefined suffix: 'your_index_name + index_name_separator + your_index_language'
        index_languages: <your_index_languages>
```
