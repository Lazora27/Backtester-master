import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und VWAPBands
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'VWAPBands': 1.0
        })
    )
