import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
