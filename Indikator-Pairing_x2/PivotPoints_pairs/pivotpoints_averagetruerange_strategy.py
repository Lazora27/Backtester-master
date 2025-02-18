import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AverageTrueRange': 1.0
        })
    )
