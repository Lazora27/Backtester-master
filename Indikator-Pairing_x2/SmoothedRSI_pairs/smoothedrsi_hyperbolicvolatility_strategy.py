import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
