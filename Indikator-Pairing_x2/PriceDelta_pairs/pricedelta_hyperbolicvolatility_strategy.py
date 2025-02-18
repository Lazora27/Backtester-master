import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
