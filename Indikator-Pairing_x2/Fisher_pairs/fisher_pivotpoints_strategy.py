import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PivotPoints
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PivotPoints': 1.0
        })
    )
