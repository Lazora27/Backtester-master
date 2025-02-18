import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'IchimokuCloud': 1.0
        })
    )
