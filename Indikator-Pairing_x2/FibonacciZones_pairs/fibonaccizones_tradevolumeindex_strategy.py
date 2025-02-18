import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
