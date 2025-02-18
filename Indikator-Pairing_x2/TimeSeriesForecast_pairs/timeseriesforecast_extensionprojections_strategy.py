import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'ExtensionProjections': 1.0
        })
    )
