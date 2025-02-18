import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
