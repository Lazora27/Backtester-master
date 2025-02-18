import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'HilbertSinewave': 1.0
        })
    )
