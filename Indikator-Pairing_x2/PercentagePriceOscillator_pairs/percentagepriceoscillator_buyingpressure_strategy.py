import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'BuyingPressure': 1.0
        })
    )
