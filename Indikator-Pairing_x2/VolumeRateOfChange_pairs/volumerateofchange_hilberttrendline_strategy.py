import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'HilbertTrendline': 1.0
        })
    )
