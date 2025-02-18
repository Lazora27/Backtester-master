import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'BuyingPressure': 1.0
        })
    )
