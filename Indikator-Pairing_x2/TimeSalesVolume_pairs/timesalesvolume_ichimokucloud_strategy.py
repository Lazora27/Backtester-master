import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'IchimokuCloud': 1.0
        })
    )
