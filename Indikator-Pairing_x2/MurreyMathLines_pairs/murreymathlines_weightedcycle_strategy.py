import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'WeightedCycle': 1.0
        })
    )
