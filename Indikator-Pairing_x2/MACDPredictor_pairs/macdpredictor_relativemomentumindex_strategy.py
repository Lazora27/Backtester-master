import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
