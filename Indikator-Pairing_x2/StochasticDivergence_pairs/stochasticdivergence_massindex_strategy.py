import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MassIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MassIndex': 1.0
        })
    )
