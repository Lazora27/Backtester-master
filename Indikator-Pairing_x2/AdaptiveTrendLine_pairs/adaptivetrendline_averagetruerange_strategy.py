import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'AverageTrueRange': 1.0
        })
    )
