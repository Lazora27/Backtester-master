import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und GannSquares
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'GannSquares': 1.0
        })
    )
