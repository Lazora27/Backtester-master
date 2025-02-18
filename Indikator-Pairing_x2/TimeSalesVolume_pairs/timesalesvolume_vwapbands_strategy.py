import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'VWAPBands': 1.0
        })
    )
