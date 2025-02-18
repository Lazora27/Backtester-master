import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
