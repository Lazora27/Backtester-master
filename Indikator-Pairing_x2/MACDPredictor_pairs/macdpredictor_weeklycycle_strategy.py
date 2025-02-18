import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'WeeklyCycle': 1.0
        })
    )
