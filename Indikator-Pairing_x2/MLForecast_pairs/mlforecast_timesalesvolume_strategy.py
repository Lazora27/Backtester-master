import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
