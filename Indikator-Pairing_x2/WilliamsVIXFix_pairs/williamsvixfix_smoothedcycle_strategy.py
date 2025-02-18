import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'SmoothedCycle': 1.0
        })
    )
