import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
