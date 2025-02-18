import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und WilliamsR
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'WilliamsR': 1.0
        })
    )
