import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VolumeProfile': 1.0
        })
    )
