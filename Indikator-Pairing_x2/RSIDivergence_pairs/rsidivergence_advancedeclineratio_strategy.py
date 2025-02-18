import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AdvanceDeclineRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AdvanceDeclineRatio
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AdvanceDeclineRatio': 1.0
        })
    )
