import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'BuyingPressure': 1.0
        })
    )
