import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SuperMACD
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SuperMACD': 1.0
        })
    )
