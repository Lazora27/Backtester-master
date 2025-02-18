import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
