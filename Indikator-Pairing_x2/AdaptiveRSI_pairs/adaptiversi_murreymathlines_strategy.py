import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MurreyMathLines': 1.0
        })
    )
