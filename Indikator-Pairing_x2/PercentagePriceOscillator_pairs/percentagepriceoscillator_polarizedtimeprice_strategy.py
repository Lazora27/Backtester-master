import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
