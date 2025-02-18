import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
