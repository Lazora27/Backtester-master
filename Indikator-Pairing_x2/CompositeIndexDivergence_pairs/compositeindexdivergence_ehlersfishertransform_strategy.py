import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
