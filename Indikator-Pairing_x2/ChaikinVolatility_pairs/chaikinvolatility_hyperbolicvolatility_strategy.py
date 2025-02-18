import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
