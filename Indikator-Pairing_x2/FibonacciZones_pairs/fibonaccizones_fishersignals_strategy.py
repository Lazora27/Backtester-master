import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und FisherSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'FisherSignals': 1.0
        })
    )
