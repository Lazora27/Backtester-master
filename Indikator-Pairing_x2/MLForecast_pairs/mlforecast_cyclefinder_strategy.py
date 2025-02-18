import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CycleFinder': 1.0
        })
    )
