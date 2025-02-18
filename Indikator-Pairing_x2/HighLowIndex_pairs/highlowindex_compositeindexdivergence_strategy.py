import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
