import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
