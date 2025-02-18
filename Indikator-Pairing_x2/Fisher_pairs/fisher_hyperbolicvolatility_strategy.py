import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
