import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
