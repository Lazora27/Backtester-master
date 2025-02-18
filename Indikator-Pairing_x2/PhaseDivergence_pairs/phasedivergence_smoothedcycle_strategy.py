import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'SmoothedCycle': 1.0
        })
    )
