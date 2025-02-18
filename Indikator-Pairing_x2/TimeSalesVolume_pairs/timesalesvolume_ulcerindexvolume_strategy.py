import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
