import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'MACDPredictor': 1.0
        })
    )
