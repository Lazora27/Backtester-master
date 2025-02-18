import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AutoFibonacci': 1.0
        })
    )
