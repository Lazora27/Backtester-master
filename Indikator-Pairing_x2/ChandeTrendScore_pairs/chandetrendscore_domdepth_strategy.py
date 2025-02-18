import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und DOMDepth
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'DOMDepth': 1.0
        })
    )
