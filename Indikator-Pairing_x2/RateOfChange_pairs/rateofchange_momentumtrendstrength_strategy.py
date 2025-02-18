import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
