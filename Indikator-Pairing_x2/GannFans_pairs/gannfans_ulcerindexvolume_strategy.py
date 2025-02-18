import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
