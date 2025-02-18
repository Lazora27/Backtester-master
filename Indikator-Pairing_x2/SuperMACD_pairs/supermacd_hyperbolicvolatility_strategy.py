import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
