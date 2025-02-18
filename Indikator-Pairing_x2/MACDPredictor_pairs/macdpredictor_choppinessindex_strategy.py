import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
