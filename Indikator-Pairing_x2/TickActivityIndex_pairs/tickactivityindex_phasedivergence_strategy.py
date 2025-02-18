import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
