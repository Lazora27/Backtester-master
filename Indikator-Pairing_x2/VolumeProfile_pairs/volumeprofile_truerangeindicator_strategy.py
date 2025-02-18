import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
