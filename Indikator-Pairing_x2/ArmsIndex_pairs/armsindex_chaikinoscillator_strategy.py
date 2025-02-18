import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
