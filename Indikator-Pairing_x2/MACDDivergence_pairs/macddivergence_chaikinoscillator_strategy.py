import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
