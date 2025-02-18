import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
