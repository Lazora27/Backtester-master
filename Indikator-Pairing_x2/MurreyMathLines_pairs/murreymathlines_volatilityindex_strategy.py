import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'VolatilityIndex': 1.0
        })
    )
