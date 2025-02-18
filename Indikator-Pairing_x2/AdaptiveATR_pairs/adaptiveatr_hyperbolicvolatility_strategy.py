import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
