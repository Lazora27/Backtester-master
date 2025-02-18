import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
