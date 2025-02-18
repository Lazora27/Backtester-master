import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
