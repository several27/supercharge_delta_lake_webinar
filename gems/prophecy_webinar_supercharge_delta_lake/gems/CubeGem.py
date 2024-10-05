from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class CubeGem(ComponentSpec):
    name: str = "CubeGem"
    category: str = "Transform"

    def optimizeCode(self) -> bool:
        return True

    @dataclass(frozen=True)
    class CubeGemProperties(ComponentProperties):
        aggregate: List[SColumnExpression] = field(default_factory=list) 
        cube: List[SColumnExpression] = field(default_factory=list)  

    def dialog(self) -> Dialog:
        return Dialog("Aggregate").addElement(
            ColumnsLayout(gap="1rem", height="100%")
                .addColumn(
                PortSchemaTabs(
                    selectedFieldsProperty="columnsSelector"
                )
                    .importSchema(),
                "2fr",
                )
                .addColumn(
                    Tabs()
                        .bindProperty("activeTab")
                        .addTabPane(
                            TabPane("Aggregate", "aggregate").addElement(
                                StackLayout(height="100%")
                                    .addElement(
                                    ExpTable("Aggregate Expressions").bindProperty("aggregate")
                                )
                            )
                        )
                        .addTabPane(
                            TabPane("Cube", "cube").addElement(
                                ExpTable("Group By Columns").bindProperty("cube")
                            )
                        ),
                    "5fr",
                
                )
        )

    def validate(self, context: WorkflowContext, component: Component[CubeGemProperties]) -> List[Diagnostic]:
        return []

    def onChange(self, context: WorkflowContext, oldState: Component[CubeGemProperties], newState: Component[CubeGemProperties]) -> Component[
    CubeGemProperties]:
        return newState


    class CubeGemCode(ComponentCode):
        def __init__(self, newProps):
            self.props: CubeGem.CubeGemProperties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            return in0\
                .agg(*map(lambda x: x.column(), self.props.aggregate)) \
                .cube(*map(lambda x: x.column(), self.props.cube)) 

   
