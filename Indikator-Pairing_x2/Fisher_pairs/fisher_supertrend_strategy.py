import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SuperTrend
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SuperTrend': 1.0
        })
    )
