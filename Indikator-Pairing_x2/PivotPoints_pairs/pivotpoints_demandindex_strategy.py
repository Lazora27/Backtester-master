import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und DemandIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'DemandIndex': 1.0
        })
    )
