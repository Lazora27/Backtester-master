import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DOMDepth
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DOMDepth': 1.0
        })
    )
