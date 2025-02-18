import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'GannSquareReversal': 1.0
        })
    )
