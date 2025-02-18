import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
