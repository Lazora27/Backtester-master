import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ParabolicSAR': 1.0
        })
    )
