import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'CenterOfGravity': 1.0
        })
    )
