import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'AverageTrueRange': 1.0
        })
    )
