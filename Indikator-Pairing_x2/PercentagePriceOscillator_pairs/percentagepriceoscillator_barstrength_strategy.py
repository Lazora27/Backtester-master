import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und BarStrength
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'BarStrength': 1.0
        })
    )
