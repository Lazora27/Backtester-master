import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'ParabolicSAR': 1.0
        })
    )
