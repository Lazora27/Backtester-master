import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AdaptiveATR': 1.0
        })
    )
