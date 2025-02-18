import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DOMDepth
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DOMDepth': 1.0
        })
    )
