import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
