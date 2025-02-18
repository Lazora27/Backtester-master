import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
