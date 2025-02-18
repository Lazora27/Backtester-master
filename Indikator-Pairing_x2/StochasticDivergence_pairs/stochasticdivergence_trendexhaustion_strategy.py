import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TrendExhaustion': 1.0
        })
    )
