import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'VWAPBands': 1.0
        })
    )
