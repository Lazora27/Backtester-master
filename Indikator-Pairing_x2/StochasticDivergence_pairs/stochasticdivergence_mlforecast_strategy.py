import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MLForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MLForecast
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MLForecast': 1.0
        })
    )
