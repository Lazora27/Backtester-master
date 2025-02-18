import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'EaseOfMovement': 1.0
        })
    )
