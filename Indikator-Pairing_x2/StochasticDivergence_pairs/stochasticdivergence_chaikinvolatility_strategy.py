import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
