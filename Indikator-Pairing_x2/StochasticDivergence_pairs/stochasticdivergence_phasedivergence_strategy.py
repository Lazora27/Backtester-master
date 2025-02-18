import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PhaseDivergence': 1.0
        })
    )
