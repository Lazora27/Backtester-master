import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PutCallRatio': 1.0
        })
    )
