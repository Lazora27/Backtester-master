import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'CenterOfGravity': 1.0
        })
    )
