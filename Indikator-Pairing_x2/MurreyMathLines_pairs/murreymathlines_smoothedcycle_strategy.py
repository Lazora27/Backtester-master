import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'SmoothedCycle': 1.0
        })
    )
