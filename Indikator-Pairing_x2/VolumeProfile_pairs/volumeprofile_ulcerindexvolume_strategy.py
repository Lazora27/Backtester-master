import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
