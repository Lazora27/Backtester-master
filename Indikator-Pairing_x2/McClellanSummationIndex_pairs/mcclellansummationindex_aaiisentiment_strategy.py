import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
