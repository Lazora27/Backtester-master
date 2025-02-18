import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MACDPredictor': 1.0
        })
    )
