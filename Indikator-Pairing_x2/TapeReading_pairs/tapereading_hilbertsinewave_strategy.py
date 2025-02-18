import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HilbertSinewave': 1.0
        })
    )
