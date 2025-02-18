import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'WeeklyCycle': 1.0
        })
    )
