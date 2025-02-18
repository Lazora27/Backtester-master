import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AdaptiveATR': 1.0
        })
    )
