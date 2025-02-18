import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'HilbertSinewave': 1.0
        })
    )
