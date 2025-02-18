import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
