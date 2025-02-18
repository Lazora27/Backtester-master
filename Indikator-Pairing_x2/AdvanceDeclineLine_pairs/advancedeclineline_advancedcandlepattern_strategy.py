import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
