import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
