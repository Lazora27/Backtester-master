import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VolatilityIndex': 1.0
        })
    )
