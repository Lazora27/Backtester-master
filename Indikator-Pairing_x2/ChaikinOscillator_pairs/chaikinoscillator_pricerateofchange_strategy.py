import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
