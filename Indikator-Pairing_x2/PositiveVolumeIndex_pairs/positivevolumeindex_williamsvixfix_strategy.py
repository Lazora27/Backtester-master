import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
