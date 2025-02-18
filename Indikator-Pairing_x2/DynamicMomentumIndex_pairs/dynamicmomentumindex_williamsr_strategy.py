import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
