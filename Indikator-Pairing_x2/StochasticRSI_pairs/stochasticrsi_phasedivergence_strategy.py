import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PhaseDivergence': 1.0
        })
    )
