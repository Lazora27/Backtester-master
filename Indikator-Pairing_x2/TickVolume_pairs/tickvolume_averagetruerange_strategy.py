import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AverageTrueRange': 1.0
        })
    )
