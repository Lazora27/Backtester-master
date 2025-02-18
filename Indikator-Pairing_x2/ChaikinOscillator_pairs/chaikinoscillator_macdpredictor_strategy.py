import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MACDPredictor': 1.0
        })
    )
