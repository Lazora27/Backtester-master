import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
