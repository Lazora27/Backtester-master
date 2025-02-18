import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
