import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
