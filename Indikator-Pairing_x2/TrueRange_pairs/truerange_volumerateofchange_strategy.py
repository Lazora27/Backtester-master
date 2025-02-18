import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
