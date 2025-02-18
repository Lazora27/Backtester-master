import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'PivotPoints': 1.0
        })
    )
