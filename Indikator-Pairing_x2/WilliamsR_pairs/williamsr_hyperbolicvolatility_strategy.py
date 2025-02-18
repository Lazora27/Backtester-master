import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
