import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
