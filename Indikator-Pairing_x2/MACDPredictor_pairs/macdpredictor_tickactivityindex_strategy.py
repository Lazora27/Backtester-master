import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TickActivityIndex': 1.0
        })
    )
