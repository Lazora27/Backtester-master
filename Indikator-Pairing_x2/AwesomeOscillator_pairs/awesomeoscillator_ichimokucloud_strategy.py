import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'IchimokuCloud': 1.0
        })
    )
