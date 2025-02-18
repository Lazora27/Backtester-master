import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und CycleFinder
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'CycleFinder': 1.0
        })
    )
