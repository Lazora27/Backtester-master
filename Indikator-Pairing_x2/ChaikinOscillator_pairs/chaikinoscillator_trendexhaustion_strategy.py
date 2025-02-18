import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'TrendExhaustion': 1.0
        })
    )
