import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'TimeCycle': 1.0
        })
    )
