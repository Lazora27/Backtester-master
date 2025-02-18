import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
