import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
