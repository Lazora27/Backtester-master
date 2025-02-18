import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
