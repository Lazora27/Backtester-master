import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
