import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'BuyingPressure': 1.0
        })
    )
