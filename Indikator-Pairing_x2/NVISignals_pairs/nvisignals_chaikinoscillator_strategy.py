import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
