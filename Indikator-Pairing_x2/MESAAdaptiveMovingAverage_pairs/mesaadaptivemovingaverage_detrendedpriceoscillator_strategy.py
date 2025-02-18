import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MESAAdaptiveMovingAverage_DetrendedPriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MESAAdaptiveMovingAverage und DetrendedPriceOscillator
    """
    
    params = (
        ('indicators', {
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            },
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            }
        }),
        ('weights', {
            'MESAAdaptiveMovingAverage': 1.0,
            'DetrendedPriceOscillator': 1.0
        })
    )
