import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_EhlersCenterOfGravityOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und EhlersCenterOfGravityOscillator
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'EhlersCenterOfGravityOscillator': 1.0
        })
    )
