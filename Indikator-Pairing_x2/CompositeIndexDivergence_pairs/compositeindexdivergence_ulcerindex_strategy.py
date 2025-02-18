import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'UlcerIndex': 1.0
        })
    )
