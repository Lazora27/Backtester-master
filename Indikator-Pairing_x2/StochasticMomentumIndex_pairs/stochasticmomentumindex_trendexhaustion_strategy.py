import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
