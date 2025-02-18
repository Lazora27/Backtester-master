import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AutoFibonacci': 1.0
        })
    )
