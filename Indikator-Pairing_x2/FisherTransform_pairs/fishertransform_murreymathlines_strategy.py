import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MurreyMathLines': 1.0
        })
    )
