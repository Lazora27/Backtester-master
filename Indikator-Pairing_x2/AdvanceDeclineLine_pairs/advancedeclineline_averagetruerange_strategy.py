import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'AverageTrueRange': 1.0
        })
    )
