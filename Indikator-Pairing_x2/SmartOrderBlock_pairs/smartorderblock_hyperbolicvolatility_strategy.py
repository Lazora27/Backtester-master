import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
