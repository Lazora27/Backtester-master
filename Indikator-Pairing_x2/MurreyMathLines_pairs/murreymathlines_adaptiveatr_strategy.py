import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'AdaptiveATR': 1.0
        })
    )
