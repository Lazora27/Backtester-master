import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und GannFans
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'GannFans': 1.0
        })
    )
