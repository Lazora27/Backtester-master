import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TickVolume
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TickVolume': 1.0
        })
    )
