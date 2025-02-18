import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
