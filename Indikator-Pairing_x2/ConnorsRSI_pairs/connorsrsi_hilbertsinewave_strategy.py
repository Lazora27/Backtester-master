import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'HilbertSinewave': 1.0
        })
    )
