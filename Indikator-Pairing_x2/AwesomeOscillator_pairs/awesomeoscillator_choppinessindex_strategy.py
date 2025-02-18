import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
