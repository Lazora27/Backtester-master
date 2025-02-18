import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
