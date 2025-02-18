import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
