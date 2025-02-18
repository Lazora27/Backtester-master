import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'IchimokuCloud': 1.0
        })
    )
