import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
