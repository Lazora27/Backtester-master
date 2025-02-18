import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'HilbertSinewave': 1.0
        })
    )
