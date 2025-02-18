import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und FisherSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'FisherSignals': 1.0
        })
    )
