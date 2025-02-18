import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'PhaseDivergence': 1.0
        })
    )
