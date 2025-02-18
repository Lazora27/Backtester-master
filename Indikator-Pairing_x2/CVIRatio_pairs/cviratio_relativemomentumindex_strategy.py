import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
