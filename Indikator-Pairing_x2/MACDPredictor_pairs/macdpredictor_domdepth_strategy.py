import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DOMDepth
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DOMDepth': 1.0
        })
    )
