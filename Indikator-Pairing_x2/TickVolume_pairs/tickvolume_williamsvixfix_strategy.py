import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
