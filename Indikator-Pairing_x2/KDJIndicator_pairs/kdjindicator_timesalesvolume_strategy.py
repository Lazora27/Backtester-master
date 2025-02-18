import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
