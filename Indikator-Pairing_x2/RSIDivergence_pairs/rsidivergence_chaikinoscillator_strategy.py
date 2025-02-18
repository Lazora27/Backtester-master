import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
