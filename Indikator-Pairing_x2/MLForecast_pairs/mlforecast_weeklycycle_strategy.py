import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'WeeklyCycle': 1.0
        })
    )
