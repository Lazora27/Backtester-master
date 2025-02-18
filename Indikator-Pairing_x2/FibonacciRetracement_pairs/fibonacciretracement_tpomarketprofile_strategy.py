import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
