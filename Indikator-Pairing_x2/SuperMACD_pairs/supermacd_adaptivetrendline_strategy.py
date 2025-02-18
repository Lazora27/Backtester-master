import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
