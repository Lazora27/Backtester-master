import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'OpenInterest': 1.0
        })
    )
