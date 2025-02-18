import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ATRTrailingStopIndicator_DetrendedPriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ATRTrailingStopIndicator und DetrendedPriceOscillator
    """
    
    params = (
        ('indicators', {
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            },
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            }
        }),
        ('weights', {
            'ATRTrailingStopIndicator': 1.0,
            'DetrendedPriceOscillator': 1.0
        })
    )
