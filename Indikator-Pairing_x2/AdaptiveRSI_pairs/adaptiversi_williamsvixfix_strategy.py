import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
