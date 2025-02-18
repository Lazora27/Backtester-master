import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
