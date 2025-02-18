import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
