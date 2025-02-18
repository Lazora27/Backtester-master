import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'MurreyMathLines': 1.0
        })
    )
