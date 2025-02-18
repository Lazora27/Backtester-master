import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'VolumeDelta': 1.0
        })
    )
