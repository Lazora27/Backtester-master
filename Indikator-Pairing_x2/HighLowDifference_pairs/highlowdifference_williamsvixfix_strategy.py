import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
