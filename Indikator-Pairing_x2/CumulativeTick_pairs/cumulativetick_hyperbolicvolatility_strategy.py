import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
