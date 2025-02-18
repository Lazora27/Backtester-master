import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'CenterOfGravity': 1.0
        })
    )
