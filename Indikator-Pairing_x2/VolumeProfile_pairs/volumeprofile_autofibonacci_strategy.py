import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AutoFibonacci': 1.0
        })
    )
