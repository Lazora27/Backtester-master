import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'VolatilityIndex': 1.0
        })
    )
