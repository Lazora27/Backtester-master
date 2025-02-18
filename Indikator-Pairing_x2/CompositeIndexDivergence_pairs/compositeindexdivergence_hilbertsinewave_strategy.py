import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'HilbertSinewave': 1.0
        })
    )
