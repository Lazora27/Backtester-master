import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ModifiedRSI': 1.0
        })
    )
