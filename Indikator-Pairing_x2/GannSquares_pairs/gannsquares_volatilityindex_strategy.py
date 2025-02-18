import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'VolatilityIndex': 1.0
        })
    )
