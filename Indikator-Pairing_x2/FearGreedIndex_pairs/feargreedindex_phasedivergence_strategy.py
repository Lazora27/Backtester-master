import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
