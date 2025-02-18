import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'SuperTrend': 1.0
        })
    )
