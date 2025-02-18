import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HilbertSinewave': 1.0
        })
    )
