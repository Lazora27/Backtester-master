import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
