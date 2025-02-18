import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
