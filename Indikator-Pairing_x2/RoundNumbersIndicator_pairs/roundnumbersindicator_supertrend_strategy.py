import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'SuperTrend': 1.0
        })
    )
