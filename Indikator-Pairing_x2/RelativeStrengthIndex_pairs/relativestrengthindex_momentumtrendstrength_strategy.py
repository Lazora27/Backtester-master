import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
