import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
