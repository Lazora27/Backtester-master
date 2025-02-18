import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
