import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'PhaseDivergence': 1.0
        })
    )
