import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'OpenInterest': 1.0
        })
    )
