import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'MACDPredictor': 1.0
        })
    )
