import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
