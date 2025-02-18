import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
