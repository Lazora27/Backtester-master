import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
