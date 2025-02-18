import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
