import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'BuyingPressure': 1.0
        })
    )
