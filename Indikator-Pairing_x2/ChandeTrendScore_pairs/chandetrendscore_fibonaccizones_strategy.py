import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FibonacciZones': 1.0
        })
    )
