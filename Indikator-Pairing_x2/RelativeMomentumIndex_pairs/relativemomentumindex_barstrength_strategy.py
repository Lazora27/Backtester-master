import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'BarStrength': 1.0
        })
    )
