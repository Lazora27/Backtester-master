import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und TrueRange
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'TrueRange': 1.0
        })
    )
