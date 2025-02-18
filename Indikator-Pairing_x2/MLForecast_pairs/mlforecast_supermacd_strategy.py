import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SuperMACD
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SuperMACD': 1.0
        })
    )
