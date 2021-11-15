from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result


class JupyterNotebookAction(ActionRunner):

    def __init__(self, **kwargs):
        pass

    async def run(self, payload):
        return Result(port="payload", value=payload)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_jupyter_notebook.plugin',
            className='JupyterNotebookAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="bartosz dobrosielski",
            init={}
        ),
        metadata=MetaData(
            name='tracardi-jupyter-notebook',
            desc='plugin to connect tracardi with jupiter notebook and run all cells',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )