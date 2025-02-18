import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
