import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DonchianChannels': 1.0
        })
    )
