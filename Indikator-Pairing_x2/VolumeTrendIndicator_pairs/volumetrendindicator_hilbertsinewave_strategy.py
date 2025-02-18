import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
