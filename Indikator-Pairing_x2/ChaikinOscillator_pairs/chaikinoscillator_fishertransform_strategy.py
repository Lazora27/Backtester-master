import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und FisherTransform
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'FisherTransform': 1.0
        })
    )
