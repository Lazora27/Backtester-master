import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
