import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AutoFibonacci': 1.0
        })
    )
