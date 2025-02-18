import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedVolatilityIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedVolatilityIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'NormalizedVolatilityIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
