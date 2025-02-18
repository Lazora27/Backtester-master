import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
