import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'TrendExhaustion': 1.0
        })
    )
