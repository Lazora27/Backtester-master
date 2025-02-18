import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
