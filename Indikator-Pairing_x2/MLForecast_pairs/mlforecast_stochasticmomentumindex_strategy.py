import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
