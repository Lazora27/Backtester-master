import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FearGreedIndex': 1.0
        })
    )
