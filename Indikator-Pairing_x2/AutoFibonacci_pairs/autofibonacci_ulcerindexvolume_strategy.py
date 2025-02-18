import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
