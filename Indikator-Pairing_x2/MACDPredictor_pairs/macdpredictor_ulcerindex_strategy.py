import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'UlcerIndex': 1.0
        })
    )
