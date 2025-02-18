import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
