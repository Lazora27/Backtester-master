import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und MassIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'MassIndex': 1.0
        })
    )
