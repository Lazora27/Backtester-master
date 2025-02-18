import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'AroonIndicator': 1.0
        })
    )
