import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'HilbertSinewave': 1.0
        })
    )
