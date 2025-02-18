import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
