import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
