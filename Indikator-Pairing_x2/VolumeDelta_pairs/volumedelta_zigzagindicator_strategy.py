import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
