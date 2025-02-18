import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
