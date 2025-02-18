import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und StreakCounter
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'StreakCounter': 1.0
        })
    )
