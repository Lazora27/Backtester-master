import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
