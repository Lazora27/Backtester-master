import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'PriceDelta': 1.0
        })
    )
