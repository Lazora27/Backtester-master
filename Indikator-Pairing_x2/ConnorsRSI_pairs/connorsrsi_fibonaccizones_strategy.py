import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'FibonacciZones': 1.0
        })
    )
