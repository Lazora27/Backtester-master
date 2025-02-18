import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ParabolicSAR': 1.0
        })
    )
