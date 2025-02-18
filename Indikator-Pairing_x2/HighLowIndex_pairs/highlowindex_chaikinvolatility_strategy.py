import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
