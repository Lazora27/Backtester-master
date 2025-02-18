import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
