import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
