import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
