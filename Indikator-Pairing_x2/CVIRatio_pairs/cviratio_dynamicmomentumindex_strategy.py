import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
