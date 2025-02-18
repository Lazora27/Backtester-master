import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
