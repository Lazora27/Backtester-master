import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
