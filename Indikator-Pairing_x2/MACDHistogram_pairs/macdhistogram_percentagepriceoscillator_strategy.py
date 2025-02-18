import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
