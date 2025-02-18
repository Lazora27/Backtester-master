import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
