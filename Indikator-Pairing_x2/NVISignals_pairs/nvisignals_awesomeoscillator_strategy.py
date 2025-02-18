import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
