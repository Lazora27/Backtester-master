import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
