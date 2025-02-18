import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
