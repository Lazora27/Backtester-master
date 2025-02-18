import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
