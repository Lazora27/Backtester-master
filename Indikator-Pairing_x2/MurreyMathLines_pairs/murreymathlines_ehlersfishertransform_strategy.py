import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
