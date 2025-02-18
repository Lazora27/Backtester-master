import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
