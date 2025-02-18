import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
