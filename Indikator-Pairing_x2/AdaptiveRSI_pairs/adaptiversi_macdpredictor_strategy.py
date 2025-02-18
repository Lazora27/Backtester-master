import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MACDPredictor': 1.0
        })
    )
