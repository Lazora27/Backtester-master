import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'EhlersDecycler': 1.0
        })
    )
