import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und SuperTrend
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'SuperTrend': 1.0
        })
    )
