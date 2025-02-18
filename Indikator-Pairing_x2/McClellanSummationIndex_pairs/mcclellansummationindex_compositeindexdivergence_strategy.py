import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
