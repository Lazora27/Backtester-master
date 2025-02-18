import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
