import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und NVISignals
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'NVISignals': 1.0
        })
    )
