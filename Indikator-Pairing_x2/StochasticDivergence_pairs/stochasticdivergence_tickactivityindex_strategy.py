import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TickActivityIndex': 1.0
        })
    )
