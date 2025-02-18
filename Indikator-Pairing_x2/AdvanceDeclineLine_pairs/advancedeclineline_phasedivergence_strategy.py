import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'PhaseDivergence': 1.0
        })
    )
