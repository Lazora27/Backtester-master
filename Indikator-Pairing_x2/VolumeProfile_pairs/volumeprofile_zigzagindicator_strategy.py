import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
