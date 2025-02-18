import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
