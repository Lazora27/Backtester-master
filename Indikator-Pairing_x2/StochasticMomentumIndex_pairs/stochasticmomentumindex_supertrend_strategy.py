import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
