import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
