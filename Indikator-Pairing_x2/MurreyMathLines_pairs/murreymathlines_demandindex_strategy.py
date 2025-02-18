import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und DemandIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'DemandIndex': 1.0
        })
    )
