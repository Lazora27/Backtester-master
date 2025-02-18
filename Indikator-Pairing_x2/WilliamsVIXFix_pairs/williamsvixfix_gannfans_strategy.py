import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und GannFans
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'GannFans': 1.0
        })
    )
