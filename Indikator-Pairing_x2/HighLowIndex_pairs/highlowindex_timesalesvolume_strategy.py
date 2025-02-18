import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
