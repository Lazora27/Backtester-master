import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'SmoothedCycle': 1.0
        })
    )
