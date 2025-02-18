import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'AverageLogRange': 1.0
        })
    )
