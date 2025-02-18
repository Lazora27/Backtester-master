import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HilbertSinewave': 1.0
        })
    )
