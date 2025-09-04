from argparse import Namespace

import pytest

from openhands.core.config import OpenHandsConfig
from openhands.resolver.issue_resolver import IssueResolver


def test_runtime_validation():
    config = OpenHandsConfig()
    args = Namespace(
        selected_repo='owner/repo',
        token='test_token',
        username='test_user',
        base_domain='github.com',
        output_dir='/tmp',
        issue_type='issue',
        issue_number=1,
        max_iterations=5,
        base_container_image=None,
        runtime_container_image=None,
        is_experimental=False,
        runtime='invalid_runtime',
    )
    with pytest.raises(ValueError, match="Invalid runtime 'invalid_runtime'"):
        IssueResolver.update_openhands_config(
            config,
            args.max_iterations,
            '/tmp/workspace',
            args.base_container_image,
            args.runtime_container_image,
            args.is_experimental,
            args.runtime,
        )


def test_build_workspace_base_without_issue_number():
    workspace = IssueResolver.build_workspace_base('/tmp', 'issue', None)
    assert workspace == '/tmp/workspace/issue_new_issue'


def test_build_workspace_base_with_issue_number():
    workspace = IssueResolver.build_workspace_base('/tmp', 'issue', 123)
    assert workspace == '/tmp/workspace/issue_123'
