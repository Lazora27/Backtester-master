import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
