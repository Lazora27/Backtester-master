import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
