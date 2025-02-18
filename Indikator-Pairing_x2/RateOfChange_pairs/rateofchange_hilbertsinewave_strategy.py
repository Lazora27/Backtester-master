import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HilbertSinewave': 1.0
        })
    )
