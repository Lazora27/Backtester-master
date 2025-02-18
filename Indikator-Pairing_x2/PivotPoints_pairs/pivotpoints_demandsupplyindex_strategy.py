import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
