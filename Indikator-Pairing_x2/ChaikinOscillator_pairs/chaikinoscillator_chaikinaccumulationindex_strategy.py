import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ChaikinAccumulationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ChaikinAccumulationIndex
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ChaikinAccumulationIndex': 1.0
        })
    )
