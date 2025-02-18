import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
