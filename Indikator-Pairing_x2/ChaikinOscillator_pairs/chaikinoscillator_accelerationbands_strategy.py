import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
