import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
