import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und TrueRange
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'TrueRange': 1.0
        })
    )
