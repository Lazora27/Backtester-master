import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
