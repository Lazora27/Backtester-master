import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceOscillator_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceOscillator und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DetrendedPriceOscillator': 1.0,
            'HilbertTrendline': 1.0
        })
    )
