import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'CycleFinder': 1.0
        })
    )
