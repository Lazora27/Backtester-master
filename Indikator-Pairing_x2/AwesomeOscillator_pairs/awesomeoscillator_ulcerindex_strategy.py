import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'UlcerIndex': 1.0
        })
    )
