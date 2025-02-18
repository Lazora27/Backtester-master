import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
