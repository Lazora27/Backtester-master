import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
