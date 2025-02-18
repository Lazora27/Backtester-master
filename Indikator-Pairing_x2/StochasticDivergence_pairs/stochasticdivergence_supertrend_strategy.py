import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SuperTrend
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SuperTrend': 1.0
        })
    )
