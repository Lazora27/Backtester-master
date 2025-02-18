import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
