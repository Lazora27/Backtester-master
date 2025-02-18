import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
