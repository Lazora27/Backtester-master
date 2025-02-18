import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'MurreyMathLines': 1.0
        })
    )
