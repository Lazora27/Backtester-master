import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
