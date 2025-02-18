import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
