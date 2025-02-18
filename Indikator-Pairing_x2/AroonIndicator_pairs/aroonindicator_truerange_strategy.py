import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und TrueRange
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'TrueRange': 1.0
        })
    )
