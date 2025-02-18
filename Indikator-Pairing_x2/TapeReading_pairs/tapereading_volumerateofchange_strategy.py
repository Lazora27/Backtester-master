import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
