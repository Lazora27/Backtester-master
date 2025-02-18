import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'FibonacciZones': 1.0
        })
    )
