import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und OpenInterest
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'OpenInterest': 1.0
        })
    )
