import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'EaseOfMovement': 1.0
        })
    )
