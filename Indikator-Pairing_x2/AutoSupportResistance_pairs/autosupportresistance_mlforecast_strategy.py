import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MLForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MLForecast
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MLForecast': 1.0
        })
    )
