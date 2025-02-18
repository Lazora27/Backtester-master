import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
