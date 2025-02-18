import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
