import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
