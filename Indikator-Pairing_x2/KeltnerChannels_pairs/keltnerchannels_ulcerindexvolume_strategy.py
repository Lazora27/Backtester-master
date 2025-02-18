import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
