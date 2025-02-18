import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HilbertSinewave': 1.0
        })
    )
