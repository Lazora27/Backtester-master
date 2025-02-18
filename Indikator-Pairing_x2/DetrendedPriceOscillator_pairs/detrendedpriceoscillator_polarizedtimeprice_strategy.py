import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceOscillator_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceOscillator und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'DetrendedPriceOscillator': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
