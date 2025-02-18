import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
