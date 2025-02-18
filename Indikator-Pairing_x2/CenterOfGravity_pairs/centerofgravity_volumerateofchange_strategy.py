import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
