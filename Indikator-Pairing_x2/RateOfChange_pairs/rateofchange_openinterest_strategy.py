import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und OpenInterest
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'OpenInterest': 1.0
        })
    )
