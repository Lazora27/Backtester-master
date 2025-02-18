import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'TrendCycles': 1.0
        })
    )
