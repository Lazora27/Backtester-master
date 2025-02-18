import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'EldersForceIndex': 1.0
        })
    )
