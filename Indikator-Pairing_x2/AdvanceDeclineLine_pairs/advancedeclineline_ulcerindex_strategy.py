import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'UlcerIndex': 1.0
        })
    )
