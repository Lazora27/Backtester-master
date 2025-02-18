import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
