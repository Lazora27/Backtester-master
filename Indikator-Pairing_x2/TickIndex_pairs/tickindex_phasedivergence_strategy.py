import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
