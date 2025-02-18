import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
