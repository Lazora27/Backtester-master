import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
