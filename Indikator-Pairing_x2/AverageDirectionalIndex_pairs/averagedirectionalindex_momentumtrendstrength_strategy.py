import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
