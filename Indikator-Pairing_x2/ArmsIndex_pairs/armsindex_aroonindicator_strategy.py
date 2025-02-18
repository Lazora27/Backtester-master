import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'AroonIndicator': 1.0
        })
    )
