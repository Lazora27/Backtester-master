import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'MACDPredictor': 1.0
        })
    )
