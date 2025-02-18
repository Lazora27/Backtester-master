import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AverageTrueRange': 1.0
        })
    )
