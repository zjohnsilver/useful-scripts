from git import Repo, GitCommandError


def delete_local_branches(repo_path: str, keep_branches: list[str]) -> None:
    never_delete_branches = ['main', 'master', 'develop']

    try:
        repo = Repo(repo_path)
        branches = [str(branch).replace('origin/', '') for branch in
                    repo.git.branch('-r').split('\n')]

        print(branches)

        for branch in branches:
            branch_name = branch.strip()
            should_delete_branch = (
                branch_name not in never_delete_branches and
                branch_name not in keep_branches and
                'HEAD' not in branch_name
            )

            if should_delete_branch:
                try:
                    repo.git.branch('-d', branch.strip())
                    print(f"Deleted branch: {branch}")
                except GitCommandError as e:
                    print(f"Could not delete branch {branch}: {e}")

    except Exception as e:
        print(f"Error: {e}")


branches_to_keep = ['main', 'master', 'feature/MDA-132-setup-failure-hook']
path_to_repo = '/Users/johnsilver/work/delfos/repositories/dagsters/moove'

delete_local_branches(
    path_to_repo,
    branches_to_keep
)
