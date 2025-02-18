import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'DonchianChannels': 1.0
        })
    )
