import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MACDPredictor': 1.0
        })
    )
