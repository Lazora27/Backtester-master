import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'KDJIndicator': 1.0
        })
    )
