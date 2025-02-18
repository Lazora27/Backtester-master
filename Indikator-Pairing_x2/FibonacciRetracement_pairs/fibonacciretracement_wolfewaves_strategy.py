import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'WolfeWaves': 1.0
        })
    )
