import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AAIISentiment': 1.0
        })
    )
