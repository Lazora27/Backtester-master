import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'ExtensionProjections': 1.0
        })
    )
