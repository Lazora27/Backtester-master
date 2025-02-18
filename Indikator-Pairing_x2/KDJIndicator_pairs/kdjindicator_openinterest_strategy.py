import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
