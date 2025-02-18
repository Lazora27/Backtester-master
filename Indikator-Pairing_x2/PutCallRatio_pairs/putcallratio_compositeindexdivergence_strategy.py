import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
