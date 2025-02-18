import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
