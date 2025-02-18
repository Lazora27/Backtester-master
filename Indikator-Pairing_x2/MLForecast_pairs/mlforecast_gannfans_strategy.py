import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und GannFans
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'GannFans': 1.0
        })
    )
