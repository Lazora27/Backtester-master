import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DOMDepth
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DOMDepth': 1.0
        })
    )
