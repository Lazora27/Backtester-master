import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
