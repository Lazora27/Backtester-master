import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
