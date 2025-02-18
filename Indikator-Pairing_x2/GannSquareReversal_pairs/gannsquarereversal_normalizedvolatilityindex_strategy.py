import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_NormalizedVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und NormalizedVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'NormalizedVolatilityIndex': 1.0
        })
    )
