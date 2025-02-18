import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
