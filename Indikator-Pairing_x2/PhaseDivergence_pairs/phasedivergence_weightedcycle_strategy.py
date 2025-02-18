import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'WeightedCycle': 1.0
        })
    )
