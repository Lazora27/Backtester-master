import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SmoothedCycle': 1.0
        })
    )
