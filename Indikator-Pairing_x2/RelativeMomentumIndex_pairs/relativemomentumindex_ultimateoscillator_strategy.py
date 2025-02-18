import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'UltimateOscillator': 1.0
        })
    )
