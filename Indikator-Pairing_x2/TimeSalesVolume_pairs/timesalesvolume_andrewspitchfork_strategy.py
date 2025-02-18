import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
