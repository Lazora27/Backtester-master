import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
