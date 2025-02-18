import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
