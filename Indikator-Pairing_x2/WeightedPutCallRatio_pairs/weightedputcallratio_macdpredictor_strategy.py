import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'MACDPredictor': 1.0
        })
    )
