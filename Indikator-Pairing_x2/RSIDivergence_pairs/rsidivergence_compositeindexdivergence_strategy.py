import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
