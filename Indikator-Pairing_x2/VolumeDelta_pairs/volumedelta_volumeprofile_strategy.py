import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'VolumeProfile': 1.0
        })
    )
