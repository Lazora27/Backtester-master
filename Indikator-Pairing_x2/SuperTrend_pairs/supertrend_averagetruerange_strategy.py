import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'AverageTrueRange': 1.0
        })
    )
