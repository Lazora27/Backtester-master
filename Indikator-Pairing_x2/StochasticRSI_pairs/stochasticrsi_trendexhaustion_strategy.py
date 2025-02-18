import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TrendExhaustion': 1.0
        })
    )
