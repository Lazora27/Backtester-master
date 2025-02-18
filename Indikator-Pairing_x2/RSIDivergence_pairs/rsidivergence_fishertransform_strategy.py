import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und FisherTransform
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'FisherTransform': 1.0
        })
    )
