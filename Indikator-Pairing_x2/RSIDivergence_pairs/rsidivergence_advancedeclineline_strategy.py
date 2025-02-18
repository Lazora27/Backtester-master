import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AdvanceDeclineLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AdvanceDeclineLine
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AdvanceDeclineLine': 1.0
        })
    )
