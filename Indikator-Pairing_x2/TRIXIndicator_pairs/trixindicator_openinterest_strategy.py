import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
