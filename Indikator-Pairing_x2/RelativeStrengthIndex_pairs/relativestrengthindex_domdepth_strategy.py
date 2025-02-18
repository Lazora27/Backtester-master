import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
