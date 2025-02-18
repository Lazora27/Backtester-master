import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AdaptiveATR': 1.0
        })
    )
