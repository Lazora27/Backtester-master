import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und TrueRange
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'TrueRange': 1.0
        })
    )
