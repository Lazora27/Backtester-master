import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und VWAPBands
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'VWAPBands': 1.0
        })
    )
