import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DemandIndex': 1.0
        })
    )
