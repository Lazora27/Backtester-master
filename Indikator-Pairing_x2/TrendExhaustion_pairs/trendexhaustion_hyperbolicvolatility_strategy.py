import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
