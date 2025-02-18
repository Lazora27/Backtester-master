import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
