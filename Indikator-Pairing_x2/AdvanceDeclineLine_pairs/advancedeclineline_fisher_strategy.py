import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und Fisher
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'Fisher': 1.0
        })
    )
