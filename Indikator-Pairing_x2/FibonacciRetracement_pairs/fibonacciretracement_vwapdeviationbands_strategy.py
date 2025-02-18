import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
