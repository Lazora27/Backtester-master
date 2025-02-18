import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
