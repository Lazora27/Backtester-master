import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und TrueRange
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'TrueRange': 1.0
        })
    )
