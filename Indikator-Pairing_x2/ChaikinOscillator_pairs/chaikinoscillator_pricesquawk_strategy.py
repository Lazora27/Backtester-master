import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
