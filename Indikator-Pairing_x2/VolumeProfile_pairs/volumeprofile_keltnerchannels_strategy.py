import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'KeltnerChannels': 1.0
        })
    )
