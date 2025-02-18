import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
