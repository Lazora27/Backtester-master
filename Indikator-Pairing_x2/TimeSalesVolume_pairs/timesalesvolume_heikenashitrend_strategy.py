import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
