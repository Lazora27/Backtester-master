import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ModifiedRSI': 1.0
        })
    )
