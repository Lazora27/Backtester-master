import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'TRIXIndicator': 1.0
        })
    )
