import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ModifiedATR': 1.0
        })
    )
