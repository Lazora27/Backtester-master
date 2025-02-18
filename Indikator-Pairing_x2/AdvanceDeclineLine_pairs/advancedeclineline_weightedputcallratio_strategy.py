import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
