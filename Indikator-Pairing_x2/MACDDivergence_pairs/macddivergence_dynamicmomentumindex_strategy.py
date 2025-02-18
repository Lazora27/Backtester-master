import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
