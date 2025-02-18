import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
