import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'SuperTrend': 1.0
        })
    )
