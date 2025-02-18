import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und WilliamsR
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'WilliamsR': 1.0
        })
    )
