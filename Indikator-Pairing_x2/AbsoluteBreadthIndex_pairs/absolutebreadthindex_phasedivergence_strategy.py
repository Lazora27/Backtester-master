import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AbsoluteBreadthIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AbsoluteBreadthIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AbsoluteBreadthIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
