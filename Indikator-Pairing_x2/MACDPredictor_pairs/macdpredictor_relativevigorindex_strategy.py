import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
