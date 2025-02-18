import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'TRIXIndicator': 1.0
        })
    )
