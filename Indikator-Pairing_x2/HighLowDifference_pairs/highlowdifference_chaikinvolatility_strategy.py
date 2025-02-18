import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
