import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
