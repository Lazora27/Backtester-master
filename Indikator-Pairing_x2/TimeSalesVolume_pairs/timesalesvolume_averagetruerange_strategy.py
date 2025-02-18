import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AverageTrueRange': 1.0
        })
    )
