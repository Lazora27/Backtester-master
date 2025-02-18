import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
