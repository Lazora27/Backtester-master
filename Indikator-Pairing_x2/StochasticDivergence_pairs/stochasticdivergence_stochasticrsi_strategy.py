import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'StochasticRSI': 1.0
        })
    )
