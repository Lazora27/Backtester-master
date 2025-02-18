import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'AutoFibonacci': 1.0
        })
    )
