import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'CenterOfGravity': 1.0
        })
    )
