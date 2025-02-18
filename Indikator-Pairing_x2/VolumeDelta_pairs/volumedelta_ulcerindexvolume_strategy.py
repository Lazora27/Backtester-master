import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
