import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'MACDPredictor': 1.0
        })
    )
