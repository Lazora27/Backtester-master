import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MomentumIndicator': 1.0
        })
    )
