import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MACDPredictor': 1.0
        })
    )
