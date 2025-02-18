import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
