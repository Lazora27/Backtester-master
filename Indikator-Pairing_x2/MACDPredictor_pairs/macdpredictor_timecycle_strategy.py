import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TimeCycle': 1.0
        })
    )
