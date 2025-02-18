import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'MurreyMathLines': 1.0
        })
    )
