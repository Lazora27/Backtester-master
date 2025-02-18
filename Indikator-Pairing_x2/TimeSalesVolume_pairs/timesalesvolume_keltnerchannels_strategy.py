import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'KeltnerChannels': 1.0
        })
    )
