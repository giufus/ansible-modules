## Ansible Modules Search Utility  

Just a little bit of scraping to quickly get what you need.  
I find it quicker than ansible-doc.
I hope it will be useful.

- build dependencies: `python3`, `requests`, `nuitka` and `bs4`  
- generate the executable (optional)
```
python -m nuitka list_modules.py
```

USAGE: source or binary
```
python list_modules.py <keyword>
```

```
list_modules.bin <keyword>
```

Sample:
```
$ python list_modules.py pipeline
 ____  ____  ____  ____  __    ____  _  _  ____
(  _ \(_  _)(  _ \( ___)(  )  (_  _)( \( )( ___)
)___/ _)(_  )___/ )__)  )(__  _)(_  )  (  )__)
(__)  (____)(__)  (____)(____)(____)(_)\_)(____)
by ansible-modules

community.aws.codepipeline – Create or delete AWS CodePipelines
https://docs.ansible.com/ansible/latest/collections/community/aws/codepipeline_module.html#ansible-collections-community-aws-codepipeline-module

community.aws.data_pipeline – Create and manage AWS Datapipelines
https://docs.ansible.com/ansible/latest/collections/community/aws/data_pipeline_module.html#ansible-collections-community-aws-data-pipeline-module

community.general.bitbucket_pipeline_key_pair – Manages Bitbucket pipeline SSH key pair
https://docs.ansible.com/ansible/latest/collections/community/general/bitbucket_pipeline_key_pair_module.html#ansible-collections-community-general-bitbucket-pipeline-key-pair-module

community.general.bitbucket_pipeline_known_host – Manages Bitbucket pipeline known hosts
https://docs.ansible.com/ansible/latest/collections/community/general/bitbucket_pipeline_known_host_module.html#ansible-collections-community-general-bitbucket-pipeline-known-host-module

community.general.bitbucket_pipeline_variable – Manages Bitbucket pipeline variables
https://docs.ansible.com/ansible/latest/collections/community/general/bitbucket_pipeline_variable_module.html#ansible-collections-community-general-bitbucket-pipeline-variable-module
```