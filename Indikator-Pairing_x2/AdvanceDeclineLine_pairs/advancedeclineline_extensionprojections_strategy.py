import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'ExtensionProjections': 1.0
        })
    )
