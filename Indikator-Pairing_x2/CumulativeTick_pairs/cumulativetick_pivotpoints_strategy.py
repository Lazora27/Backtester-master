import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und PivotPoints
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'PivotPoints': 1.0
        })
    )
