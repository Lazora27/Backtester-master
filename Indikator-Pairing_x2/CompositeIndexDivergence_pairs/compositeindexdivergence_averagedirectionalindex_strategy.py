import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
