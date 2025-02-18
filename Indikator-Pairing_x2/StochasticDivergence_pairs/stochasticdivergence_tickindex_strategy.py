import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TickIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TickIndex': 1.0
        })
    )
