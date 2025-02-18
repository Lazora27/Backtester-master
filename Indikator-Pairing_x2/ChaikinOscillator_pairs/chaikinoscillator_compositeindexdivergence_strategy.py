import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
