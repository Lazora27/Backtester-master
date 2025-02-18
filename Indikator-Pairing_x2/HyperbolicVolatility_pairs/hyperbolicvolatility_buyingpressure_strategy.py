import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'BuyingPressure': 1.0
        })
    )
