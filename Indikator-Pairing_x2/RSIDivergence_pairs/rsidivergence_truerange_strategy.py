import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TrueRange
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TrueRange': 1.0
        })
    )
