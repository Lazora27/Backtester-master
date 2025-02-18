import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'AverageLogRange': 1.0
        })
    )
