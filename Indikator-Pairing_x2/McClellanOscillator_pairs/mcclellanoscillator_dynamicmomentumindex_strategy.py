import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
