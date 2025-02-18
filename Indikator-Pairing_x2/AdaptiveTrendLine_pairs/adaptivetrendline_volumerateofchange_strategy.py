import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
