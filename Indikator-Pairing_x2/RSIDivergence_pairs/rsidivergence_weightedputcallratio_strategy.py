import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
