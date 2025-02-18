import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
