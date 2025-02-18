import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
