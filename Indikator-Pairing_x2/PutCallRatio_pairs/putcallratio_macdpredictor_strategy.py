import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MACDPredictor': 1.0
        })
    )
