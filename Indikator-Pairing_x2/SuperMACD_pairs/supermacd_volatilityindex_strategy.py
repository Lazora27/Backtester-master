import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VolatilityIndex': 1.0
        })
    )
