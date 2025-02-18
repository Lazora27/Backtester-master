import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
