import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ArmsIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ArmsIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ArmsIndex': 1.0
        })
    )
