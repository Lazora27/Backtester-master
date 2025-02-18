import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
